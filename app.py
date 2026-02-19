import cv2
import os
import shutil
import base64
import numpy as np
import joblib
import pandas as pd
from flask import Flask, request, render_template, jsonify, redirect
from datetime import date, datetime
from sklearn.neighbors import KNeighborsClassifier

app = Flask(__name__)

# Constants
IMAGES_TO_CAPTURE = 10
FACE_CASCADE_PATH = 'haarcascade_frontalface_default.xml'

# Set up directories
today = date.today().strftime("%m_%d_%y")
attendance_date = date.today().strftime("%d-%B-%Y")

attendance_dir = 'Attendance'
os.makedirs(attendance_dir, exist_ok=True)

static_dir = 'static'
faces_dir = os.path.join(static_dir, 'faces')
os.makedirs(faces_dir, exist_ok=True)

attendance_file = os.path.join(attendance_dir, f'Attendance-{today}.csv')
if not os.path.exists(attendance_file):
    with open(attendance_file, 'w') as f:
        f.write('Name,Roll,Time')

# Load face detector
face_detector = cv2.CascadeClassifier(FACE_CASCADE_PATH)

# ================= Helper Functions =================

def total_registered_users():
    if not os.path.exists(faces_dir): return 0
    return len(os.listdir(faces_dir))

def get_registered_users():
    if not os.path.exists(faces_dir): return []
    users = []
    for user_folder in os.listdir(faces_dir):
        if '_' in user_folder:
            parts = user_folder.split('_')
            if len(parts) >= 2:
                name = parts[0]
                user_id = parts[1]
                users.append({'name': name, 'id': user_id, 'folder': user_folder})
    return users

def extract_faces(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_points = face_detector.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
    return face_points

def identify_face(face_array):
    model_path = os.path.join(static_dir, 'face_recognition_model.pkl')
    if not os.path.exists(model_path):
        return None
    model = joblib.load(model_path)
    return model.predict(face_array)

def train_model_logic():
    faces = []
    labels = []
    
    if not os.path.exists(faces_dir) or not os.listdir(faces_dir):
         # Remove model if no faces
        if os.path.exists(os.path.join(static_dir, 'face_recognition_model.pkl')):
            os.remove(os.path.join(static_dir, 'face_recognition_model.pkl'))
        return False

    user_list = os.listdir(faces_dir)
    for user in user_list:
        user_dir = os.path.join(faces_dir, user)
        if not os.path.isdir(user_dir): continue
        for image_file in os.listdir(user_dir):
            try:
                img = cv2.imread(os.path.join(user_dir, image_file))
                if img is None: continue
                resized_face = cv2.resize(img, (50, 50))
                faces.append(resized_face.ravel())
                labels.append(user)
            except: pass
    
    if not faces: 
        if os.path.exists(os.path.join(static_dir, 'face_recognition_model.pkl')):
            os.remove(os.path.join(static_dir, 'face_recognition_model.pkl'))
        return False
    
    faces = np.array(faces)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(faces, labels)
    joblib.dump(knn, os.path.join(static_dir, 'face_recognition_model.pkl'))
    return True

def extract_attendance():
    if not os.path.exists(attendance_file):
        return [], [], [], 0
    try:
        df = pd.read_csv(attendance_file)
        names = df['Name'].tolist()
        rolls = df['Roll'].tolist()
        times = df['Time'].tolist()
        return names, rolls, times, len(df)
    except:
        return [], [], [], 0

def add_attendance_record(name):
    # Safe split in case of weird folder names
    parts = name.split('_')
    username = parts[0]
    user_id = parts[1] if len(parts) > 1 else 'Unknown'
    
    current_time = datetime.now().strftime("%H:%M:%S")

    df = pd.read_csv(attendance_file)
    if 'Roll' in df.columns and user_id.isdigit():
        if int(user_id) not in list(df['Roll']):
            with open(attendance_file, 'a') as f:
                f.write(f'\n{username},{user_id},{current_time}')
            return True, current_time
    else:
        # Fallback for non-numeric IDs or corrupted CSV
         with open(attendance_file, 'a') as f:
            f.write(f'\n{username},{user_id},{current_time}')
         return True, current_time

    return False, current_time

def decode_image(data_url):
    header, encoded = data_url.split(",", 1)
    data = base64.b64decode(encoded)
    np_arr = np.frombuffer(data, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    return img

# ================= Routes =================

@app.route('/')
def home():
    names, rolls, times, attendance_count = extract_attendance()
    return render_template('home.html', names=names, rolls=rolls, times=times, l=attendance_count,
                           totalreg=total_registered_users(), 
                           users=get_registered_users(),
                           datetoday2=attendance_date)

@app.route('/start')
def start():
    # Render the attendance taking page
    if 'face_recognition_model.pkl' not in os.listdir(static_dir):
        names, rolls, times, attendance_count = extract_attendance()
        return render_template('home.html', names=names, rolls=rolls, times=times, l=attendance_count,
                               totalreg=total_registered_users(), 
                               users=get_registered_users(),
                               datetoday2=attendance_date,
                               mess='No trained model found. Please add a new face first.')
    return render_template('attendance.html')

@app.route('/add', methods=['POST'])
def add():
    # Receive form data and render the capture page
    new_username = request.form['newusername']
    new_user_id = request.form['newuserid']
    return render_template('add_user.html', newusername=new_username, newuserid=new_user_id)

@app.route('/delete_user', methods=['POST'])
def delete_user():
    folder_name = request.form['user_folder']
    path = os.path.join(faces_dir, folder_name)
    if os.path.exists(path):
        import shutil
        try:
            shutil.rmtree(path)
            train_model_logic() # Retrain or clear model
        except Exception as e:
            print(f"Error deleting user {folder_name}: {e}")
            
    return redirect('/')

# ================= API Endpoints =================

@app.route('/api/mark_attendance', methods=['POST'])
def api_mark_attendance():
    data = request.json
    if 'image' not in data:
        return jsonify({'status': 'error', 'message': 'No image data'}), 400
    
    img = decode_image(data['image'])
    faces = extract_faces(img)
    
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        # Convert numpy int32 to python int for JSON serialization
        face_loc = [int(x), int(y), int(w), int(h)]
        
        face_img = cv2.resize(img[y:y+h, x:x+w], (50, 50))
        result = identify_face(face_img.reshape(1, -1))
        
        if result is not None:
            identified_person = result[0]
            added, time = add_attendance_record(identified_person)
            return jsonify({
                'status': 'success', 
                'user': identified_person, 
                'time': time, 
                'newly_marked': added, 
                'face_location': face_loc
            })
            
    return jsonify({'status': 'unknown'})

@app.route('/api/add_face', methods=['POST'])
def api_add_face():
    data = request.json
    username = data['username']
    userid = data['userid']
    count = data['count']
    img = decode_image(data['image'])
    
    user_image_folder = os.path.join(faces_dir, f'{username}_{userid}')
    os.makedirs(user_image_folder, exist_ok=True)
    
    faces = extract_faces(img)
    if len(faces) > 0:
        (x, y, w, h) = faces[0]
        save_img = img[y:y+h, x:x+w]
        image_name = f"{username}_{count}.jpg"
        cv2.imwrite(os.path.join(user_image_folder, image_name), save_img)
        return jsonify({'status': 'success'})
    
    return jsonify({'status': 'retry', 'message': 'No face detected'})

@app.route('/api/train_model', methods=['POST'])
def api_train_model():
    success = train_model_logic()
    if success:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': 'Training failed'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))
