import numpy as np
import cv2 as cv

def val_change(x) :
    print(x);

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('Blue', 'image', 0, 255, val_change)
cv.createTrackbar('Green', 'image', 0, 255, val_change)
cv.createTrackbar('Red', 'image', 0, 255, val_change)

switch = '0: OFF\n 1 : ON'
cv.createTrackbar(switch, 'image', 0, 1, val_change)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    b = cv.getTrackbarPos('Blue', 'image')
    g = cv.getTrackbarPos('Green', 'image')
    r = cv.getTrackbarPos('Red', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]



cv.destroyAllWindows()
