import cv2

ESC = 27
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('video.mp4', fourcc, 30, (640, 480))

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    # 影像大小必須與設定一致，否則會輸出失敗
    out.write(frame)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ESC: 
        cv2.destroyAllWindows()
        break
