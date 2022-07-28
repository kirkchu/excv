import cv2 
import numpy as np

gc = np.zeros((512, 512, 3), dtype=np.uint8)
gc.fill(255)

#cv2.line(gc, (10, 50), (400, 300), (255, 0, 0), 5)
# cv2.rectangle(gc, (30, 50), (200, 280), (0, 0, 255), 5)
# cv2.rectangle(gc, (100, 200), (196, 276), (234, 151, 102), -1)
# cv2.circle(gc, (200, 100), 80, (255, 255, 0), -1)
# cv2.circle(gc, (280, 180), 60, (147, 113, 217), 3)
# cv2.ellipse(gc, (200, 100), (80, 40), 45, 0, 360, (80, 127, 255), 5)
# cv2.ellipse(gc, (250, 200), (70, 70), 0, 0, 135, (44, 141, 108), -1)

#設定頂點座標
# pts = np.array(((10,5), (100,100), (170,120), (200,50)))
#True:頭尾相連; False:頭尾不相連
# cv2.polylines(gc, [pts], True, (105, 105, 105), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(gc, 'OpenCV', (10,200), font, 4, (0,0,0), 2, cv2.LINE_AA)

cv2.imshow('draw', gc) 
cv2.waitKey(0)
cv2.destroyAllWindows()