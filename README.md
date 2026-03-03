
<p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x"></p></p><p class="MuiTypography-root MuiTypography-bodyMedium MuiTypography-paragraph css-14g3j2x">&lt;p align="center"&gt;
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
