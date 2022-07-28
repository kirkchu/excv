import cv2

src = cv2.imread('pipe.jpg')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, None, 10, 75, 3, 75)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT_ALT, 1, 10, None, 10, 0.8, 3, 40)

if circles is not None:
    circles = circles.astype(int)
    img = src.copy()
    print(circles)
    for c in circles[0]:
        x, y, r = c
        # 畫圓
        cv2.circle(img, (x, y), r, (0, 0, 255), 3)
        # 畫圓心
        cv2.circle(img, (x, y), 2, (0, 255, 0), 3)

    src = cv2.hconcat([src, img])
    cv2.imshow('image', src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
