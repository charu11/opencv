import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 1280) # 3 is the associated number for the width
cap.set(4, 720) # 4 is the associated number for the height

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()) :
    ret, frame = cap.read()
    if ret == True:

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", grey)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
            break

cap.release()
cv2.destroyAllWindows()
