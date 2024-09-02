import cv2
import numpy as np
import os
from gtts import gTTS
import pygame
pygame.mixer.init()

# First initialize YOLOv4-tiny model
net = cv2.dnn.readNet("Oculus/dnn_model/yolov4-tiny.weights", "Oculus/dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

# Load class names (you can remove some of them in the classes.txt file)
classes = []
with open("Oculus/dnn_model/classes.txt", "r") as file:
    for class_name in file.readlines():
        classes.append(class_name.strip())

# Initializing camera
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

# Preload audio files if they're not already loaded from a previous execution
audio_files = {}

# Create window with the button that activates the audio-mode
cv2.namedWindow('Oculus')
button = False #Start with the button not pressed

def click_button(event, x, y, f, a):  #Function to click the button
    global button
    if event == cv2.EVENT_LBUTTONDOWN:
        rectangle = np.array([(20, 20), (220, 20), (220, 70), (20, 70)])
        inside = cv2.pointPolygonTest(rectangle, (x, y), False)
        if inside > 0:
            button = not button  # Change button state

cv2.setMouseCallback("Oculus", click_button)

# Main loop of Oculus
while True:
    ret, frame = cam.read() #Read from camera

    if not ret:
        break

    # Draw the green button
    polygon = np.array([(20, 20), (220, 20), (220, 70), (20, 70)])
    cv2.polylines(frame, [polygon], isClosed=True, color=(0, 255, 0), thickness=2)
    cv2.fillPoly(frame, [polygon], color=(0, 255, 0, 0.3))  # Green polygon filled

    # Starting the detection
    (class_ids, scores, boxes) = model.detect(frame)

    for class_id, score, box in zip(class_ids, scores, boxes):
        if score > 0.5:  # If it's more than 50% sure
            class_name = classes[class_id]  # Using the class id to identify the class in the list
            if button and class_name not in audio_files:
                # Generate an audio file if it doesn't exist yet
                name = class_name + ".mp3"
                tts = gTTS(text=f"I see a {class_name}", lang='en', slow=True)
                tts.save(name)
                audio_files[class_name] = name
            
            if button and class_name in audio_files and not pygame.mixer.music.get_busy():
                # Reproduce the audio if it already exists
                pygame.mixer.music.load(audio_files[class_name])
                pygame.mixer.music.play()

            # Draw bounding box and label
            x, y, w, h = box
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 3)
            cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)

    # Instruction messages
    cv2.putText(frame, "Press the green button to activate the audio mode ;)", (750, 70), cv2.FONT_HERSHEY_PLAIN, 1, (0, 128, 0), 2)
    cv2.putText(frame, "Press q to exit", (750, 90), cv2.FONT_HERSHEY_PLAIN, 1, (0, 128, 0), 2)

    # Show it
    cv2.imshow("Oculus", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Close when q is pressed
        break

# Clean up
cam.release()
cv2.destroyAllWindows()











