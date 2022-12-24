import cv2

def overlayAlpha(original, overlay):
    overlay_rgb = overlay[:,:,0:3]
    overlay_alpha = overlay[:,:,3:]
    
    overlay_mask = cv2.threshold(overlay_alpha, 0, 255, cv2.THRESH_BINARY)[1]
    overlay_out = cv2.bitwise_and(overlay_rgb, overlay_rgb, mask=overlay_mask)

    original_mask = cv2.bitwise_not(overlay_mask)
    original_out = cv2.bitwise_and(original, original, mask=original_mask)
    return cv2.add(overlay_out, original_out)
    
def overlay(original, overlay):
    overlay_mask = cv2.cvtColor(overlay, cv2.COLOR_BGR2GRAY)
    overlay_mask = cv2.threshold(overlay_mask, 250, 255, cv2.THRESH_BINARY_INV)[1]
    overlay_out = cv2.bitwise_and(overlay, overlay, mask=overlay_mask)

    original_mask = cv2.bitwise_not(overlay_mask)
    original_out = cv2.bitwise_and(original, original, mask=original_mask)
    return cv2.add(overlay_out, original_out)
    
original_image = cv2.imread('original.jpg')
overlay_image = cv2.imread('overlay.png', -1)
newsize = (original_image.shape[1], original_image.shape[0])
overlay_image = cv2.resize(overlay_image, newsize)

if overlay_image.shape[2] == 4:
    image = overlayAlpha(original_image, overlay_image)
else:
    image = overlay(original_image, overlay_image)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
