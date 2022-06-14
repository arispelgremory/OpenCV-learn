import cv2 as cv
import numpy as np

# Blank img
# uint8 / unsigned 8 bit integers = blank img
blankImg = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blankImg)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# paint img with color
blankImg[200: 300, 300:400] = 0, 255, 255
cv.imshow("Yellow", blankImg)

# 2. Draw a Rectangle
cv.rectangle(blankImg, (0, 0), (blankImg.shape[1] // 2, blankImg.shape[0] // 2), (0, 255, 255), thickness=-1)
cv.imshow('Rectangle', blankImg)

# 3. Draw a circle
cv.circle(blankImg, (250, 250))

cv.waitKey(0)