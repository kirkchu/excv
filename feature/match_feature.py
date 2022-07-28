import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i1', '--image1', required=True,
    help='first image')
ap.add_argument('-i2', '--image2', required=True,
    help='second image')
args = vars(ap.parse_args())

img1 = cv2.imread(args['image1'], 0)
img2 = cv2.imread(args['image2'], 0)

feature = cv2.xfeatures2d.SIFT_create()
kp1, des1 = feature.detectAndCompute(img1, None)
kp2, des2 = feature.detectAndCompute(img2, None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

good = []
for m, n in matches:
    if m.distance < 0.50 * n.distance:
        good.append(m)
print('Matching points :{}'.format(len(good)))
img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, outImg=None, flags=2)

width, height, channel = img3.shape
ratio = float(width) / float(height)
img3 = cv2.resize(img3, (1024, int(1024 * ratio)))
cv2.imshow('video', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
