import cv2 as cv

# ------------------------------- #

# Rescale frame ( only can resize smaller)

def rescaleFrame(frame, scale=0.75):
    # Works with image, video and live video

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeResolution(width, height):
    # Only works for live videos
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread('Photos/cat_large.jpg')
img_resized = rescaleFrame(img, .1)

cv.imshow('Cat', img_resized)
cv.waitKey(0)

# capture = cv.VideoCapture('Videos/dog.mp4')

# while True:
#     # read frame by frame
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame, .2)

#     cv.imshow('Video', frame)

#     cv.imshow('Video Resized', frame_resized)

#     if(cv.waitKey(20) & 0xFF==ord('d')):
#         break

# capture.release()
# cv.destroyAllWindows()