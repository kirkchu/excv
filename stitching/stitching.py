import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('img', nargs='+', help = 'input images')
args = ap.parse_args()

imgs = []
for img_name in args.img:
    img = cv2.imread(img_name)
    imgs.append(img)

stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
status, pano = stitcher.stitch(imgs)

if status == cv2.Stitcher_OK:
    h, w, c = pano.shape
    ratio = w / h
    pano = cv2.resize(pano, (1024, int(1024 / ratio)))
    cv2.imshow('image', pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('done')
else:
    print('error: {}'.format(status))
