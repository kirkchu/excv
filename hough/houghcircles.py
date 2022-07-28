import cv2
import numpy as np

src = cv2.imread('cup.jpg')
src = cv2.resize(src, (403, 302))
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, None, 10, 75, 3, 75)
print(circles)
if circles is not None:
    circles = circles.astype(int)
    img = src.copy()
    for x, y, r in circles[0]:
        # 畫圓
        cv2.circle(img, (x, y), r, (0, 0, 255), 3, cv2.LINE_AA)
        # 畫圓心
        cv2.circle(img, (x, y), 2, (0, 255, 0), 3, cv2.LINE_AA)

    src = cv2.hconcat([src, img])
    cv2.imshow('image', src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
