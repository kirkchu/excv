import cv2
cap = cv2.VideoCapture('vtest.avi')
bg = cap.read()[1]
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2GRAY)
bg = cv2.GaussianBlur(bg, (17, 17), 0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (17, 17), 0)

    diff = cv2.absdiff(gray, bg)
    diff = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)[1]
    diff = cv2.erode(diff, None, iterations=2)
    diff = cv2.dilate(diff, None, iterations=2)
    #cv2.imshow('test', diff)

    cnts, hierarchy = cv2.findContours(
        diff, 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)
    
    for c in cnts:
        if cv2.contourArea(c) < 500:
            continue

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)

    cv2.imshow("frame", frame)

    if cv2.waitKey(100) == 27:
        cv2.destroyAllWindows()
        break
