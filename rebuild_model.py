import os
import cv2
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Constants matching app.py
static_dir = 'static'
faces_dir = os.path.join(static_dir, 'faces')

def train_model():
    faces = []
    labels = []
    
    if not os.path.exists(faces_dir):
        print(f"Error: Directory {faces_dir} does not exist.")
        return

    user_list = os.listdir(faces_dir)
    print(f"Found users: {user_list}")
    
    if not user_list:
        print("No users found to train on.")
        return

    for user in user_list:
        user_dir = os.path.join(faces_dir, user)
        if not os.path.isdir(user_dir):
            continue
            
        print(f"Processing user: {user}")
        for image_file in os.listdir(user_dir):
            image_path = os.path.join(user_dir, image_file)
            try:
                img = cv2.imread(image_path)
                if img is None:
                    print(f"Warning: Could not read image {image_path}")
                    continue
                resized_face = cv2.resize(img, (50, 50))
                faces.append(resized_face.ravel())
                labels.append(user)
            except Exception as e:
                print(f"Error processing {image_path}: {e}")

    if not faces:
        print("No valid face data found.")
        return

    faces = np.array(faces)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(faces, labels)
    
    output_path = os.path.join(static_dir, 'face_recognition_model.pkl')
    joblib.dump(knn, output_path)
    print(f"Model trained and saved to {output_path}")

if __name__ == '__main__':
    train_model()
