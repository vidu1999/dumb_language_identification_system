import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
import os
import tkinter as tk
from tkinter import messagebox
import threading

selected_recognizer = None

model_paths = [
    os.path.abspath("wordnov6.task"),
    os.path.abspath("letter.task"),
    os.path.abspath("number.task")
]

recognizers = [vision.GestureRecognizer.create_from_model_path(model_path) for model_path in model_paths]

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def camera_feed():
    global selected_recognizerq

    cap = cv2.VideoCapture(1)

    with mp_hands.Hands(model_complexity=1, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while cap.isOpened():
            success, frame = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue


            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                    h, w, _ = frame.shape
                    bbox_coords = [
                        min(int(hand_landmark.x * w) for hand_landmark in hand_landmarks.landmark),
                        min(int(hand_landmark.y * h) for hand_landmark in hand_landmarks.landmark),
                        max(int(hand_landmark.x * w) for hand_landmark in hand_landmarks.landmark),
                        max(int(hand_landmark.y * h) for hand_landmark in hand_landmarks.landmark)
                    ]

                    x_min, y_min, x_max, y_max = bbox_coords
                    cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)

                    if selected_recognizer:
                        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)


                        recognition_result = selected_recognizer.recognize(mp_image)

                        if recognition_result.gestures:
                            top_gesture = recognition_result.gestures[0][0]


                            gesture_text = f"Gesture: {top_gesture.category_name} ({top_gesture.score:.2f})"


                            text_position = (x_min, y_min - 10)
                            cv2.putText(frame, gesture_text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

            cv2.imshow('Gesture Recognition', frame)

            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

def select_model(model_index):
    global selected_recognizer
    selected_recognizer = recognizers[model_index]
    messagebox.showinfo("Model Selection", f"Model {model_index + 1} selected")

def start_camera_thread():
    camera_thread = threading.Thread(target=camera_feed)
    camera_thread.daemon = True
    camera_thread.start()

root = tk.Tk()
root.title("Real-time Gesture Recognition Model Selector")

btn_model_1 = tk.Button(root, text="Word", command=lambda: select_model(0), width=25, height=2)
btn_model_2 = tk.Button(root, text="Letter", command=lambda: select_model(1), width=25, height=2)
btn_model_3 = tk.Button(root, text="number", command=lambda: select_model(2), width=25, height=2)

btn_model_1.pack(pady=10)
btn_model_2.pack(pady=10)
btn_model_3.pack(pady=10)

start_camera_thread()

root.mainloop()
