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
  - [OpenCV](https://opencv.org/) – 🎥 Video capture & processing  
  - [Mediapipe](https://developers.google.com/mediapipe) – ✋ Hand landmark detection  
  - [PyAutoGUI](https://pyautogui.readthedocs.io/) – 🖱️ Mouse automation  
  - [Tkinter](https://docs.python.org/3/library/tkinter.html) – 🖼️ GUI window  
  - [Pillow](https://python-pillow.org/) – 🖌️ Image handling inside Tkinter  

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

**📦 Project Root** → Virtual-Mouse-Using-Hand-Gesture/  
**📄 Main Script** → virtual_mouse.py  
**📄 Dependencies** → requirements.txt  
**📄 Documentation** → README.md  
**⚙️ Git Ignore** → .gitignore  
**📂 Virtual Environment** → .venv/ (not committed)  

## 🔧 Installation & Setup  
**1️⃣ Clone the Repository** → git clone https://github.com/yourusername/Virtual-Mouse-Using-Hand-Gesture.git , 
**cd Virtual-Mouse-Using-Hand-Gesture**

**2️⃣ Create Virtual Environment**  **python -m venv .venv**
**source .venv/bin/activate #on (Linux/Mac** 
**.venv\Scripts\activate #0n (Windows)**  

**3️⃣ Install Dependencies** 
**opencv-python**
**mediapipe**
**pyautogui**
**pillow**
then install: pip install -r requirements.txt  

**4️⃣ Run the Project** → python virtual_mouse.py  

---

## 🎮 Controls  
🖐️ **Move Cursor** → Move your thumb in front of the camera  
👆 **Click** → Bring thumb & index finger close together  
🔴 **Exit** → Close the Tkinter window to stop the program  

---

## 📸 Demo  
👍 **Thumb movement** → Cursor moves  
👆 **Thumb + Index close** → Left-click  

---

## 🧩 Notes  
**Recommended Python version** → 3.9.x  
**Virtual environment** → Uses .venv for isolation  
**.gitignore** → Skips __pycache__/ , .venv/ , *.pyc , *.pyo , *.dll etc.  
