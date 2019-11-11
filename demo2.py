import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('out.avi', fourcc, 20.0, (640,480)) # the 4 arguments are name of the output, fourcc code, frame per mili second, and the frame size
print((cap.isOpened()))
while(cap.isOpened()) :
    ret, frame = cap.read()
    if ret == True :
        # to get width and the height of the frame
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)

        # turn the image into grey colour
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', grey)

        if cv2.waitKey(1) == ord('q'):
            break

    else :
        break

cap.release()
out.release()
cv2.destroyAllWindows()

