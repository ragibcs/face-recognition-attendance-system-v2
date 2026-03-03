# Face Recognition Attendance System

<p align="center"> <img src="Images/attendence.png" alt="Attendance System Demo" width="800">

<p align="center"> <a href="https://github.com/ragibcs/face-recognition-attendance-system-v2"> <img src="https://img.shields.io/github/license/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge" alt="License"> </a> <a href="https://github.com/ragibcs/face-recognition-attendance-system-v2"> <img src="https://img.sh
---

## Features | Feature | Description | |---------|-------------| | 🤖 **Auto Face Detection** | Haar Cascades for real-time face detection | | 👤 **Face Recognition** | KNN-based machine learning model for precise user identification | | 📊 **Attendance Logging** | Automatic CSV logging with name, roll, and timestamp |
| 🌐 **Web Interface** | User management with a clean Flask-powered UI | | 🔄 **Auto Model Training** | When users are added, the model automatically rebuilds |

## Technology Stack

<p align="left"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"> <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV"> <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn"> <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas"> <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">

### Launch the Application ```bash python app.py```

Next, launch the browser at **`http://localhost:5000`**.
---

## 📁 Project Structure ``` face-recognition-attendance-system-v2/ → app.py                              # Rebuild_model.py is the main Flask application. # requirements.txt is the model training script.                    The file haarcascade_frontalface_default.xml contains the following dependencies: Python; LICENSE; MIT License; README.md; this file; the face detector; static; faces; and user face images; face_recognition_model.In pkl, the machine learning model is trained. The HTML templates are as follows: home.html; add_user.html; attendance.html; Attendance/; Daily CSV logs; Images/; Project assets; attendance.png

---

## Licensing

The **MIT License** governs this project; for more information, refer to the [LICENSE](LICENSE) file.
---

<p align="center"> Created with ❤️ by <a href="https://github.com/ragibcs">ragibcs</a>
