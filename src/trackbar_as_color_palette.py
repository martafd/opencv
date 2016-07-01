import cv2
import numpy as np

img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')

def nothing(x):
   pass

cv2.createTrackbar('r', 'image', 0, 255, nothing)
cv2.createTrackbar('g', 'image', 0, 255, nothing)
cv2.createTrackbar('b', 'image', 0, 255, nothing)
# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    r = cv2.getTrackbarPos('r','image')
    g = cv2.getTrackbarPos('g','image')
    b = cv2.getTrackbarPos('b','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()