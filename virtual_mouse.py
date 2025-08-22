import cv2
import tkinter as tk
from PIL import Image, ImageTk
import pyautogui
import mediapipe as mp
import math

# Screen size
screen_width, screen_height = pyautogui.size()

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)
cam_width = 640
cam_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, cam_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_height)

# Tkinter window setup
window = tk.Tk()
window.overrideredirect(True)
window.wm_attributes("-topmost", True)
window.geometry(f"{cam_width}x{cam_height}+0+0")

label = tk.Label(window)
label.pack()

def update():
    ret, frame = cap.read()
    if not ret:
        return

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)
    h, w, _ = frame.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get index and thumb tip coordinates
            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            ix, iy = int(index_tip.x * w), int(index_tip.y * h)
            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)

            # Draw circles around tips
            cv2.circle(frame, (ix, iy), 10, (0, 255, 0), cv2.FILLED)     # Green for index
            cv2.circle(frame, (tx, ty), 10, (0, 255, 255), cv2.FILLED)     # Blue for thumb

            # Move mouse using thumb
            screen_x = int(thumb_tip.x * screen_width)
            screen_y = int(thumb_tip.y * screen_height)
            pyautogui.moveTo(screen_x, screen_y)

            # Check distance for click
            distance = math.hypot(ix - tx, iy - ty)
            if distance < 40:
                pyautogui.click()
                pyautogui.sleep(1)

    # Convert to tkinter image
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    window.after(10, update)

update()
window.mainloop()
cap.release()
