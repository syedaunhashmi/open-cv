import  cv2
import numpy as np

img = cv2.imread('1 (2).jpeg')
cap = cv2.VideoCapture(0)
while 1:
    _,frame = cap.read()
    new_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.imshow('img', new_img)
    lower = np.array([163, 50, 50])
    uper = np.array([183, 252, 255])
    mask = cv2.inRange(new_img, lower, uper)
    cv2.imshow('mask', mask)
    res = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('result', res)
    k=cv2.waitKey(5)& 0xFF
    if k== 27:
        break


cv2.destroyAllWindows