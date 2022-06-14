import cv2 as cv

# Reading img
# catImg = cv.imread('Photos/cat_large.jpg')
# cv.imshow('Cat', catImg)
# cv.waitKey(0)

# ------------------------------- #
# Reading Videos
# 0 <-- reference to webcam
# capture = cv.VideoCapture(0)
# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     # read frame by frame
#     isTrue, frame = capture.read()
#     cv.imshow('Video', frame)

#     if(cv.waitKey(20) & 0xFF==ord('d')):
#         break

# capture.release()
# cv.destroyAllWindows()

# ------------------------------- #

# Rescale frame ( only can resize smaller)

catImg = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', catImg)