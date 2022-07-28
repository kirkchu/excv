from colorfilters.colorfilters import HSVFilter
import cv2 as cv

img = cv.imread('demo.jpg')

height, width, channel = img.shape
ratio = width / height
width = 300
height = int(width / ratio)
img = cv.resize(img, (width, height))

window = HSVFilter(img)
window.show()

print(window.lowerb)
print(window.upperb)
