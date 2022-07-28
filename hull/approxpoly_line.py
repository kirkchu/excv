import cv2

frame = cv2.imread('line.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50, 150)
edged = cv2.dilate(edged, None, iterations=1)

contours, hierarchy = cv2.findContours(
    edged, 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

edged = cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)
cv2.drawContours(edged, contours, -1, (0, 255, 0), 5)

print('=== 處理前')
print('點數量：{}'.format(len(contours[0])))

approx_line = cv2.approxPolyDP(contours[0], 50, True)

print('=== 處理後')
print('點數量：{}'.format(len(approx_line)))

cv2.drawContours(frame, approx_line, -1, (0, 0, 255), 5)
cv2.line(frame, approx_line[0][0], approx_line[1][0], (255, 0, 0), 3)

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
