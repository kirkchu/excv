import cv2

frame = cv2.imread('coin.jpg')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (13, 13), 0)
edged = cv2.Canny(gray, 40, 120)

contours, hierarchy = cv2.findContours(
    edged, 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

out = cv2.cvtColor(edged, cv2.COLOR_GRAY2BGR)
cv2.drawContours(out, contours, -1, (0, 255, 128), 2)

frame = cv2.hconcat([frame, out])
cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

