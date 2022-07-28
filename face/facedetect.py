import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
image = cv2.imread('demo.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#faces = face_cascade.detectMultiScale(gray, 1.1, 3)
faces = face_cascade.detectMultiScale(gray, 1.05, 20)
for (x, y, w, h) in faces:
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.imshow('video', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
