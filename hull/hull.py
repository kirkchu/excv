import cv2

frame = cv2.imread('hull.png')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50, 150)
edged = cv2.dilate(edged, None, iterations=1)
contours, hierarchy = cv2.findContours(
    edged, 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
cnt = cv2.approxPolyDP(cnt, 30, True)

hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print('凸點數量：{}'.format(len(hull)))
print('凹點數量：{}'.format(len(defects)))
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(frame,start,end,[0,255,0],2)
    cv2.circle(frame,far,5,[0,0,255],-1)

cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
