import cv2

image = cv2.imread('demo.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)[1]

#mode = cv2.RETR_TREE
mode = cv2.RETR_EXTERNAL

#method = cv2.CHAIN_APPROX_NONE
method = cv2.CHAIN_APPROX_SIMPLE

contours, hierarchy = cv2.findContours(binary, mode, method) 
#print(hierarchy)

cv2.drawContours(image, contours, -1, (0,255,0), 2)
#cv2.drawContours(image, contours, 3, (0,0,255), 2)

#cv2.drawContours(image, contours, 0, (0,0,255), 2) #紅色
#cv2.drawContours(image, contours, 1, (0,255,0), 2) #綠色
#cv2.drawContours(image, contours, 2, (255,0,0), 2) #藍色

#for p in contours[0]:
#    cv2.circle(image, tuple(p[0]), 5, (0, 0, 255), 2, -1)

cv2.imshow('image', image)
cv2.waitKey(0)
