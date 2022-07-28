import cv2

ESC = 27

def roiarea(frame, rect):
    (left, top), (right, bottom) = rect
    return frame[top:bottom, left:right]
        
def replaceroi(frame, roi, rect):
    (left, top), (right, bottom) = rect
    frame[top:bottom, left:right] = roi 
    return frame

def overlay(original_image, overlay_image):
    overlay_image_rgb = overlay_image[:,:,:3]
    overlay_image_alpha = overlay_image[:,:,3:]

    overlay_mask = cv2.threshold(overlay_image_alpha, 0, 255, cv2.THRESH_BINARY)[1]
    original_mask = cv2.bitwise_not(overlay_mask)

    fig1 = cv2.bitwise_and(original_image, original_image, mask=original_mask)
    fig2 = cv2.bitwise_and(overlay_image_rgb, overlay_image_rgb, mask=overlay_mask)
    return cv2.add(fig1, fig2)

cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) 
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cartoon = cv2.imread('cartoon.png', cv2.IMREAD_UNCHANGED)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 10)
    for (x, y, w, h) in faces:
        rect = ((x, y), (x + w, y + h))
        new_cartoon = cv2.resize(cartoon, (w, h))
        roi = roiarea(frame, rect)
        roi = overlay(roi, new_cartoon)
        frame = replaceroi(frame, roi, rect)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ESC: 
        cv2.destroyAllWindows()
        break
