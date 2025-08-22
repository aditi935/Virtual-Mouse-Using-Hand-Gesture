# 🖥️ Virtual Mouse Using Hand Gesture ✋ 

A **Virtual Mouse System** built with **Python, OpenCV, Mediapipe, and Tkinter** that allows users to control the mouse pointer using **hand gestures** captured by a webcam.  

👉 In this project:  
- The **thumb** is used to control the **cursor movement**.  
- When the **thumb and index finger come close together**, a **mouse click** is triggered.  

This system provides an innovative example of **Human-Computer Interaction (HCI)** and eliminates the need for a physical mouse.  

---

## ✨ Features  

✅ **Real-Time Cursor Control** – Move the pointer by moving your thumb.  
✅ **Click Gesture** – Left-click when the thumb and index finger tips come close.  
✅ **Visual Feedback** – Live camera feed with hand landmarks drawn on it.  
✅ **Cross-Platform** – Works on Windows, Linux, and macOS.  
✅ **Tkinter Integration** – Runs inside a lightweight fullscreen Tkinter window.  

---

## 🛠️ Tech Stack  

- **Programming Language**: Python 3.9+ 🐍  
- **Libraries & Tools**:  
  - [OpenCV](https://opencv.org/) – Video capture & processing  
  - [Mediapipe](https://developers.google.com/mediapipe) – Hand landmark detection  
  - [PyAutoGUI](https://pyautogui.readthedocs.io/) – Mouse automation  
  - [Tkinter](https://docs.python.org/3/library/tkinter.html) – GUI window  
  - [Pillow](https://python-pillow.org/) – Image handling inside Tkinter  

---

## ⚙️ How It Works  

1. **Webcam Capture** → Captures live video using OpenCV.  
2. **Hand Detection** → Mediapipe detects **21 hand landmarks** in real-time.  
3. **Cursor Movement** → Thumb tip position is mapped to the **screen resolution** using PyAutoGUI.  
4. **Click Event** → Distance between thumb tip and index tip is calculated.  
   - If distance `< 40 pixels` → a **left-click** event is triggered.  
5. **GUI Window** → Tkinter displays the video feed with hand tracking overlays.  

---

## 📂 Project Structure  

Virtual-Mouse-Using-Hand-Gesture/
│── virtual_mouse.py # Main script
│── requirements.txt # Dependencies
│── README.md # Documentation
│── .gitignore # Ignore cache & binaries
│── .venv/ # Virtual environment (not committed)

---

## 🔧 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/Virtual-Mouse-Using-Hand-Gesture.git
cd Virtual-Mouse-Using-Hand-Gesture
2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv .venv
source .venv/bin/activate      # On Linux/Mac
.venv\Scripts\activate         # On Windows

3️⃣ Install Dependencies

Add this to requirements.txt:

opencv-python
mediapipe
pyautogui
pillow


Install with:

pip install -r requirements.txt

4️⃣ Run the Project
python virtual_mouse.py

🎮 Controls

🖐️ Move Cursor → Move your thumb in front of the camera.

👆 Click → Bring thumb & index finger close together.

🔴 Exit → Close the Tkinter window to stop the program.

📸 Demo
Gesture	Action
👍 Thumb movement	Cursor moves
👆 Thumb + Index close	Left-click

(Add screenshots or GIFs of your project here)

🚀 Future Improvements

🔹 Add right-click & double-click gestures.
🔹 Implement drag & drop functionality.
🔹 Add scrolling gestures.
🔹 Improve accuracy with adaptive distance thresholds.

🤝 Contributing

Contributions are welcome! 🎉

Fork the repo

Create a new branch (feature-xyz)

Commit changes

Submit a pull request

📜 License

This project is licensed under the MIT License – free to use and modify.

🧩 Notes

Recommended Python version: 3.9.x

This project uses a .venv virtual environment for isolation.

A .gitignore is included to skip unnecessary files:

__pycache__/

.venv/

*.pyc, *.pyo, *.dll, etc.


---


