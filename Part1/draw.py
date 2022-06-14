import cv2 as cv
import numpy as np

# Blank img
# uint8 / unsigned 8 bit integers = blank img
blankImg = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blankImg)

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img)

# 1. paint img with color
blankImg[200: 300, 300:400] = 0, 255, 255
cv.imshow("Yellow", blankImg)

# 2. Draw a Rectangle
cv.rectangle(blankImg, (0, 0), (blankImg.shape[1] // 2, blankImg.shape[0] // 2), (0, 255, 255), thickness=-1)
cv.imshow('Rectangle', blankImg)

# 3. Draw a circle
cv.circle(blankImg, (blankImg.shape[1] // 2, blankImg.shape[0] // 2), 40, (0, 0, 255), thickness=-1)
cv.imshow('Circle', blankImg)

# 4. Draw a line
# arg2 = start point, args3 = end point
cv.line(blankImg, (100, 250), (300, 400), (255, 255, 255), thickness=3)
cv.imshow('Line', blankImg)

# 5. Write text
cv.putText(blankImg, "Hello World", (0, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', blankImg)

cv.waitKey(0)