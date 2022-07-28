import cv2
import time

ESC = 27

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    begin_time = time.time()
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    cv2.imshow('frame', frame)
    print('{:.3f}'.format(1 / (time.time() - begin_time)))

    if cv2.waitKey(1) == ESC: 
        cv2.destroyAllWindows()
        break
