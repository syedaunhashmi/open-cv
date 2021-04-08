import  cv2
import numpy as np

# img = cv2.imread('sample.jpg',0)
# thresh= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,20)
# cv2.imshow('dad',thresh)
# cv2.imshow('d4ad',img)
#cv2.waitKey(0)

cap = cv2.VideoCapture(0)
while 1:
    _,frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = frame.astype('uint8')
    thresh = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 91, 20)
    cv2.imshow('dad', thresh)
    cv2.imshow('d4ad', frame)

    k=cv2.waitKey(5)& 0xFF
    if k== 27:
        break
cv2.destroyAllWindows()

