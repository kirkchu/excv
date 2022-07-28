import cv2

bs = cv2.createBackgroundSubtractorMOG2()
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    gray = bs.apply(frame)
    mask = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)[1]
    mask = cv2.erode(mask, None, iterations=10)
    mask = cv2.dilate(mask, None, iterations=20)

    cnts, hierarchy = cv2.findContours(
        mask, 
        cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        if cv2.contourArea(c) < 200:
            continue
        # 畫出輪廓
        cv2.drawContours(frame, cnts, -1, (0,255,255), 10)
        # 畫出矩型
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 10)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR) 
    frame = cv2.hconcat([frame, mask])
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break
        
