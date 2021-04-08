
import time
import cv2
import numpy as np
import math

theta=0
minLineLength = 3
maxLineGap = 7
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
# cap.set(cv2.CAP_PROP_FPS, 30)

while 1:
    # ret ,frame = cap.read()
    image = cv2.imread("0 (2).jpeg")
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.GaussianBlur(gray, (55, 55), 0)
    edged = cv2.Canny(blurred, 10  , 10)
    lines = cv2.HoughLinesP(edged, 1, np.pi / 180, 10, minLineLength, maxLineGap)
    print(lines)
    cv2.imshow('Lanes Detection', edged)
    if (lines!=None):
        for x in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[x]:
                cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                theta = theta + math.atan2((y2 - y1), (x2 - x1))
    threshold = 6
    if (theta > threshold):
        print("left")
    if (theta < -threshold):

        print("right")
    if (abs(theta) < threshold):

        print( "straight")
    theta = 0
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break





