
<p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x"></p></p><p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x">&lt;p align="center"&gt;<div align="center">

# 👁️ FaceTrack v2

### **Attendance. Automated. Instantly.**

> Real-time face recognition that logs who's present — no badges, no swipes, no headaches.

[![License](https://img.shields.io/github/license/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge)](https://github.com/ragibcs/face-recognition-attendance-system-v2)
[![Stars](https://img.shields.io/github/stars/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge)](https://github.com/ragibcs/face-recognition-attendance-system-v2)
[![Forks](https://img.shields.io/github/forks/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge)](https://github.com/ragibcs/face-recognition-attendance-system-v2)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

</div>

---

## 🎬 Demo

> 📸 *Screenshot / GIF of the system in action goes here*

![Demo placeholder](Images/attendence.png)

---

## ✨ What It Does

FaceTrack v2 replaces manual attendance tracking with a live computer-vision pipeline. Point a camera at a room — it identifies faces, matches them to registered users, and writes a timestamped CSV record. All of this happens through a clean web UI with zero command-line friction for end users.

| Feature | What You Get |
|---|---|
| **⚡ Real-Time Face Detection** | Instant detection via Haar Cascades — no lag, no fuss |
| **🎯 KNN Face Recognition** | Accurate identity matching from a trained K-Nearest Neighbors model |
| **📋 Attendance Logging** | Name, roll number, and timestamp saved to a daily CSV automatically |
| **🌐 Web Interface** | Add/manage users through a simple Flask UI — no CLI needed |
| **🔄 Auto Model Retraining** | Recognition model updates itself every time a new user is added |

---

## 🧠 How It Works

```
┌─────────────────────────────────────────────────────────┐
│                      CAMERA FEED                        │
└──────────────────────────┬──────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────┐
│             FACE DETECTION  (Haar Cascades)              │
│   Scans each frame and crops detected face regions       │
└──────────────────────────┬───────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────┐
│           FACE RECOGNITION  (KNN Classifier)             │
│   Compares face embeddings against registered users      │
└──────────────────────────┬───────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────┐
│             ATTENDANCE LOGGING  (CSV via pandas)         │
│   Writes name + roll number + timestamp to daily file    │
└──────────────────────────────────────────────────────────┘
                           │
                           ▼
┌──────────────────────────────────────────────────────────┐
│              WEB UI  (Flask + HTML Templates)            │
│   View attendance, manage users, trigger retraining      │
└──────────────────────────────────────────────────────────┘
```

**New user added?** → Face images are captured → `rebuild_model.py` retrains the KNN → system is immediately updated. No manual steps required.

---

## 🚀 Getting Started

### 1. Clone & install

```bash
git clone https://github.com/ragibcs/face-recognition-attendance-system-v2.git
cd face-recognition-attendance-system-v2
pip install -r requirements.txt
```

### 2. Run

```bash
python app.py
```

### 3. Open in your browser

```
http://localhost:5000
```

That's it. Three steps and you're live.

---

## 📁 Project Structure

```
face-recognition-attendance-system-v2/
│
├── app.py                               # 🚀 Main Flask app — start here
├── rebuild_model.py                     # 🔄 Retrains the KNN recognition model
├── requirements.txt                     # 📦 All dependencies
├── haarcascade_frontalface_default.xml  # 🔍 Haar Cascade for face detection
│
├── static/
│   ├── faces/                           # 🗃️ Stored face images per user
│   └── face_recognition_model.pkl       # 🧠 Serialized trained model
│
├── templates/                           # 🌐 HTML pages
│   ├── home.html
│   ├── add_user.html
│   └── attendance.html
│
├── Attendance/                          # 📋 Daily attendance CSVs
└── Images/                              # 🖼️ Project assets
```

---

## 🗺️ Roadmap

Here's what's coming next:

- [ ] 🔒 **Anti-spoofing** — detect printed photos / screen attacks
- [ ] 📊 **Analytics dashboard** — attendance trends and statistics
- [ ] 📧 **Email/SMS alerts** — notify when a user is marked present or absent
- [ ] 🗄️ **Database backend** — replace CSV storage with SQLite/PostgreSQL
- [ ] 📱 **Mobile-friendly UI** — responsive redesign for tablets and phones
- [ ] 🐳 **Docker support** — one-command deployment

Have an idea? [Open an issue](https://github.com/ragibcs/face-recognition-attendance-system-v2/issues) and let's talk.

---

## 🤝 Contributing

Contributions are welcome and appreciated. Here's the flow:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/your-idea`
3. **Commit** your changes: `git commit -m "Add: your feature"`
4. **Push** to your branch: `git push origin feature/your-idea`
5. **Open a Pull Request** — describe what you built and why

Please keep PRs focused (one feature or fix per PR) and make sure existing functionality still works before submitting.

---

## 📝 License

Distributed under the **MIT License** — use it, fork it, ship it. See [`LICENSE`](LICENSE) for details.

---

<div align="center">

Made with ❤️ by [ragibcs](https://github.com/ragibcs)

*If this helped you, consider leaving a ⭐ — it means a lot.*

</div>
  &lt;a href="https://github.com/ragibcs/face-recognition-attendance-system-v2"&gt;</p><pre><code>&amp;lt;img src="https://img.shields.io/github/license/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge" alt="License"&amp;gt;</code></pre><p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x">&lt;a href="https://github.com/ragibcs/face-recognition-attendance-system-v2"&gt;</p><pre><code>&amp;lt;img src="https://img.shields.io/github/stars/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge" alt="Stars"&amp;gt;</code></pre><p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x">&lt;a href="https://github.com/ragibcs/face-recognition-attendance-system-v2"&gt;</p><pre><code>&amp;lt;img src="https://img.shields.io/github/forks/ragibcs/face-recognition-attendance-system-v2?style=for-the-badge" alt="Forks"&amp;gt;</code></pre><p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x"></p><hr><h2 class="MuiTypography-root MuiTypography-headingMedium css-qp7i24" id="features">Features</h2><table class="MuiTable-root css-j72mkp"><thead class="MuiTableHead-root css-1cetel5"><tr class="MuiTableRow-root MuiTableRow-head css-kknebi"><th style="text-align: start; padding: 0px 16px;"> Feature                </th><th style="text-align: start; padding: 0px 16px;"> Description                                                          </th></tr></thead><tbody class="MuiTableBody-root css-1xnox0e"><tr class="MuiTableRow-root css-kknebi"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> <strong>Automatic Face Detection</strong> </td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> Detects faces in real time with Haar Cascades.                  </td></tr><tr class="MuiTableRow-root css-kknebi"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> <strong>Face Recognition</strong>         </td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> Identifies users accurately using a KNN model.                  </td></tr><tr class="MuiTableRow-root css-kknebi"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> <strong>Attendance Logging</strong>       </td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> Saves attendance records (name, roll number, timestamp) in CSV. </td></tr><tr class="MuiTableRow-root css-kknebi"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> <strong>Web Interface</strong>            </td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> Manage users through a simple Flask-based web UI.               </td></tr><tr class="MuiTableRow-root css-kknebi"><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> <strong>Automatic Model Training</strong> </td><td class="MuiTableCell-root MuiTableCell-body MuiTableCell-sizeMedium css-1secajh"> Updates the recognition model whenever users are added.         </td></tr></tbody></table><h2 class="MuiTypography-root MuiTypography-headingMedium css-qp7i24" id="technology-stack">Technology Stack</h2><p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x">&lt;p align="left"&gt;
  &lt;img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" alt="Python"&gt;
  &lt;img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&amp;logo=flask&amp;logoColor=white" alt="Flask"&gt;
  &lt;img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&amp;logo=opencv&amp;logoColor=white" alt="OpenCV"&gt;
  &lt;img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&amp;logo=scikit-learn&amp;logoColor=white" alt="scikit-learn"&gt;
  &lt;img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&amp;logo=pandas&amp;logoColor=white" alt="pandas"&gt;
  &lt;img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&amp;logo=numpy&amp;logoColor=white" alt="NumPy"&gt;
<p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x"></p></p><h2 class="MuiTypography-root MuiTypography-headingMedium css-qp7i24" id="-getting-started">🚀 Getting Started</h2><h3 class="MuiTypography-root MuiTypography-headingSmall css-1akoz7" id="installation">Installation</h3><pre><code class="lang-bash"># Clone this repository
git clone https://github.com/ragibcs/face-recognition-attendance-system-v2.git

# Move into the project directory
cd face-recognition-attendance-system-v2

# Install all required Python packages
pip install -r requirements.txt
</code></pre>
<h3 class="MuiTypography-root MuiTypography-headingSmall css-1akoz7" id="running-the-app">Running the App</h3><pre><code class="lang-bash">python app.py
</code></pre>
<p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x">Once started, open your browser and go to: <strong><code>http://localhost:5000</code></strong></p><hr><h2 class="MuiTypography-root MuiTypography-headingMedium css-qp7i24" id="-folder-structure">📁 Folder Structure</h2><pre><code>face-recognition-attendance-system-v2/
├── app.py                              # Main Flask application file
├── rebuild_model.py                    # Script for training the recognition model
├── requirements.txt                    # List of dependencies
├── LICENSE                             # MIT License information
├── README.md                           # Project documentation
├── haarcascade_frontalface_default.xml # Haar Cascade XML for face detection
│
├── static/
│   ├── faces/                          # Directory for stored face images
│   └── face_recognition_model.pkl      # Serialized model file
│
├── templates/                          # Web templates (HTML)
│   ├── home.html
│   ├── add_user.html
│   └── attendance.html
│
├── Attendance/                         # Stores daily attendance CSV files
│
└── Images/                             # Project assets and images
    └── attendence.png
</code></pre>
<hr><h2 class="MuiTypography-root MuiTypography-headingMedium css-qp7i24" id="-license">📝 License</h2><p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x">This project is distributed under the <strong>MIT License</strong>. See the <a href="LICENSE" target="_blank" rel="noreferrer">LICENSE</a> file for more details.</p><hr><p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x">&lt;p align="center"&gt;
  Made with ❤️ by &lt;a href="https://github.com/ragibcs"&gt;ragibcs
<p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x"></p></p><hr></div>
