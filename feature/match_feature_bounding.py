import cv2
import numpy as np
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
    if m.distance < 0.55 * n.distance:
        good.append(m)

if len(good)>10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
    matchesMask = mask.ravel().tolist()
    h,w = img1.shape
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)
    img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    img2 = cv2.polylines(img2,[np.int32(dst)],True,(110,255,170),3, cv2.LINE_AA)

print('Matching points :{}'.format(len(good)))

img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, outImg=None, flags=2)
width, height, channel = img3.shape
ratio = float(width) / float(height)
img3 = cv2.resize(img3, (1024, int(1024 * ratio)))

cv2.imshow('video', img3)
cv2.waitKey(0)
input()
cv2.destroyAllWindows()
