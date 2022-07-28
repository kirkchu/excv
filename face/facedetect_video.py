import cv2
from roilib import *

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    right_frame = roiarea(frame)

    gray = cv2.cvtColor(right_frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x + left, y), (x + w + left, y + h), (0, 255, 255), 3)

    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 10)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break


