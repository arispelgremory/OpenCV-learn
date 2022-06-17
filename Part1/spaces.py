import cv2 as cv
import matplotlib.pyplot as plt

# OpenCV defaults read colors by BGR
img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# BGR is invertion of RGB
# Matplotlib shows RGB by default
# plt.imshow(img)
# plt.show()

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

plt.imshow(rgb)
plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr', hsv_bgr)

cv.waitKey(0)