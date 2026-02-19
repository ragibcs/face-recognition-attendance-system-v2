# Face Recognition Attendance System

<p align="center">
  <img src="Images/attendence.png" alt="Attendance System Demo" width="800">
</p>

<p align="center">
  <a href="https://github.com/ragibcs/face-recognition-attendance-system-v2">
    <img src="https://img.shields.io/github/license/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge" alt="License">
  </a>
  <a href="https://github.com/ragibcs/face-recognition-attendance-system-v2">
    <img src="https://img.shields.io/github/stars/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge" alt="Stars">
  </a>
  <a href="https://github.com/ragibcs/face-recognition-attendance-system-v2">
    <img src="https://img.shields.io/github/forks/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge" alt="Forks">
  </a>
</p>

---

## Features

| Feature | Description |
|---------|-------------|
| 🤖 **Auto Face Detection** | Real-time face detection using Haar Cascades |
| 👤 **Face Recognition** | KNN-based ML model for accurate user identification |
| 📊 **Attendance Logging** | Automatic CSV logging with name, roll & timestamp |
| 🌐 **Web Interface** | Clean Flask-powered UI for user management |
| 🔄 **Auto Model Training** | Model rebuilds automatically when users are added |

## Tech Stack

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn">
  <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas">
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">
</p>

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/ragibcs/face-recognition-attendance-system-v2.git

# Navigate to directory
cd face-recognition-attendance-system-v2

# Install dependencies
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Then open your browser at: **`http://localhost:5000`**

---

## 📁 Project Structure

```
face-recognition-attendance-system-v2/
├── app.py                              # Main Flask application
├── rebuild_model.py                    # Model training script
├── requirements.txt                    # Python dependencies
├── LICENSE                             # MIT License
├── README.md                           # This file
├── haarcascade_frontalface_default.xml # Face detector
│
├── static/
│   ├── faces/                          # User face images
│   └── face_recognition_model.pkl      # Trained ML model
│
├── templates/                          # HTML templates
│   ├── home.html
│   ├── add_user.html
│   └── attendance.html
│
├── Attendance/                         # Daily CSV logs
│
└── Images/                            # Project assets
    └── attendence.png
```

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/ragibcs">ragibcs</a>
</p>
