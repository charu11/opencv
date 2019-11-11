import cv2

# ............read the image.................

img = cv2.imread('lena.jpg', 0)
print(img)

# ...............show the image................
cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:

    cv2.destroyAllWindows()

elif k == ord('s'):
    # .............write the image...................
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()