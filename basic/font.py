import numpy as np
import cv2

#建立 512x512 的黑色畫布
gc = np.zeros((512, 512, 3), np.uint8)
#用(B, G, R) = (255, 255, 255): 白色填滿畫布
gc.fill(255)

font = [
    cv2.FONT_HERSHEY_SIMPLEX,
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_TRIPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX
]

y = 50
for f in font:
    cv2.putText(gc, 'OpenCV', (10,y), f, 2, (0,0,0), 2, cv2.LINE_AA)
    y += 60

cv2.imshow("draw", gc)
cv2.waitKey(0)
cv2.destroyAllWindows()
