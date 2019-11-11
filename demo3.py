import cv2

img = cv2.imread('lena.jpg', 1)

img = cv2.line(img, (0, 0), (255, 255), (0, 0, 123), 10)
img = cv2.arrowedLine(img, (0, 255), (255, 255), (137, 0, 0), 10)

img = cv2.rectangle(img, (164, 153), (357, 299), (0, 0, 200), 10)
img = cv2.circle(img, (292, 263), 99, (255, 243, 124), 10, -1)

font = cv2.FONT_HERSHEY_DUPLEX
img = cv2.putText(img, '1234567890', (10, 500), font, 2, (0, 255, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)