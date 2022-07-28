#!/Users/ckk/venv/cv/bin/python3
import cv2
import mjpglib

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

streaming = mjpglib.Streaming()

while True:
    ret, frame = cap.read()
    streaming.write(frame)
    
#    cv2.imshow('frame', frame)
#    if cv2.waitKey(1) == 27: 
#        break
