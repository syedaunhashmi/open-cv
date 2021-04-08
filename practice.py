import cv2
import numpy as np


img = cv2.imread('train.jpeg',1)
blur= cv2.blur(img,(5,5))
gb = cv2.GaussianBlur(img,(5,5),1)
matrix = np.ones((5,5),np.float32)/25
new = cv2.filter2D(img , -1 , matrix)
cv2.imshow('fff',blur)
cv2.imshow('gb',gb)
cv2.imshow('grrrb',img)
cv2.waitKey(0)