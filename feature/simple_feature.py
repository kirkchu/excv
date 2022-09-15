import cv2, argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True,
    help='image filename')
args = vars(ap.parse_args())

gray = cv2.imread(args['image'], 0)
feature = cv2.xfeatures2d.SIFT_create()
#feature = cv2.xfeatures2d.SURF_create()
#feature = cv2.ORB_create()

kp = feature.detect(gray)
#print(kp)
print('keypoints: {}'.format(len(kp)))
gray = cv2.drawKeypoints(
    gray, kp, None, 
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)
cv2.imshow('image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
