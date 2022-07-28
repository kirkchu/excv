RECT = ((960+5, 0+5), (1920-10+5, 1080-10+5))
(left, top), (right, bottom) = RECT

def roiarea(frame):
    return frame[top:bottom, left:right]
    
def replaceroi(frame, roi):
    frame[top:bottom, left:right] = roi 
    return frame
