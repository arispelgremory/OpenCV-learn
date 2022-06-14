from email import iterators
import cv2 as cv

img = cv.imread('Photos/anya.jpeg')
cv.imshow("Anya", img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur image
# The higher the arg2, the blurer the img will be
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# Resize 
# Will distort image
# add third arg if resizing huge resolution by adding interpolation=cv.INNER_CUBIC
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

# Cropping
cropped = img[50: 200, 200: 400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)