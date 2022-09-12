import cv2

frame = cv2.imread('demo.jpeg', 0)
frame = cv2.resize(frame, (5, 3))
cv2.imshow('image', frame)
print(frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
