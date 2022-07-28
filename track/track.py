import cv2

cap = cv2.VideoCapture('vtest.avi')
tracker = cv2.TrackerCSRT_create()
roi = None
while True:
    ret, frame = cap.read()
 
    if roi is None:
        roi = cv2.selectROI('frame', frame)
        if roi != (0, 0, 0, 0):
            tracker.init(frame, roi)

    success, rect = tracker.update(frame)
    if success: 
        (x, y, w, h) = [int(i) for i in rect]
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(66) == 27:
        cv2.destroyAllWindows()
        break
