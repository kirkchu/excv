import cv2

RECT, HEXAGON = 0, 1
frame = cv2.imread('poly.png')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50, 150)
edged = cv2.dilate(edged, None, iterations=1)
contours, hierarchy = cv2.findContours(
    edged, 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

print('=== 處理前')
print('矩形點數量：{}'.format(len(contours[RECT])))
print('六邊形點數量：{}'.format(len(contours[HEXAGON])))

approx_rect = cv2.approxPolyDP(contours[RECT], 30, True)
approx_hex = cv2.approxPolyDP(contours[HEXAGON], 30, True)

print('=== 處理後')
print('矩形點數量：{}'.format(len(approx_rect)))
print('六邊形點數量：{}'.format(len(approx_hex)))

cv2.drawContours(frame, [approx_rect], -1, (0, 0, 255), 5)
cv2.drawContours(frame, [approx_hex], -1, (0, 0, 255), 5)

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
