# Play video using OpenCV in python
import cv2


cap = cv2.VideoCapture("VIDEO_TITLE.mp4")

while(cap.isOpened()):
    ret, img = cap.read()

    if ret == True:
        cv2.imshow("WINDOW_TITLE", img)
        
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()

