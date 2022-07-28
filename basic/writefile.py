import cv2, time

cap = cv2.VideoCapture(0)
time.sleep(3)

ret, frame = cap.read()
if ret:
    cv2.imwrite("image.jpeg", frame)
else:
    print('讀取影像失敗')

