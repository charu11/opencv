import numpy as np
import cv2 as cv

def val_change(x):
    pass;

cv.namedWindow('tracking')

cv.createTrackbar('LH', 'tracking', 0, 255, val_change) # LH- lower hue
cv.createTrackbar('LS', 'tracking', 0, 255, val_change) # LS- lower saturation
cv.createTrackbar('LV', 'tracking', 0, 255, val_change) # LV- lower value

cv.createTrackbar('UH', 'tracking', 255, 255, val_change)
cv.createTrackbar('US', 'tracking', 255, 255, val_change)
cv.createTrackbar('UV', 'tracking', 255, 255, val_change)

while True :

    frame = cv.imread('smarties.png')
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    low_hue = cv.getTrackbarPos('LH', 'tracking')
    low_sat = cv.getTrackbarPos('LS', 'tracking')
    low_val = cv.getTrackbarPos('LV', 'tracking')

    up_hue = cv.getTrackbarPos('UH', 'tracking')
    up_sat = cv.getTrackbarPos('US', 'tracking')
    up_val = cv.getTrackbarPos('UV', 'tracking')

    low_bound = np.array([low_hue, low_sat, low_val])
    up_bound = np.array([up_hue, up_sat, up_val])

    mask = cv.inRange(hsv, low_bound, up_bound)

    res = cv.bitwise_and(frame, frame, mask = mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    key = cv.waitKey(1)
    if key == 27:
        break


cv.destroyAllWindows()



