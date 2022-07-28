import cv2
import time

ESC = 27
SPACE = 32

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

font = cv2.FONT_HERSHEY_SIMPLEX
isCountDown = False
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    if isCountDown:
        t = 5 - int(time.time() - begin_time)
        if t == 0:
            cv2.imwrite('mypicture.jpg', frame)
            cv2.destroyAllWindows()
            break

        cv2.putText(frame, str(t), (200, 350), font, 10, (0, 0, 255), 10)

    cv2.imshow('frame', frame)

    key = cv2.waitKey(1)
    if key == SPACE:
        begin_time = time.time()
        isCountDown = True
    elif key == ESC: 
        cv2.destroyAllWindows()
        break
