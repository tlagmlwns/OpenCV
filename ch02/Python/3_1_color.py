import cv2
import numpy as np

img1 = np.empty((200, 640), dtype=np.uint8)#grayscale image
img2 = np.zeros((200, 640, 3), dtype=np.uint8)#color image
img3 = np.ones((200, 640), dtype=np.uint8) * 255 #white
img4 = np.full((200, 640, 3),(0, 255, 255), dtype=np.uint8)#yellow

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)
cv2.waitKey()
cv2.destroyAllWindows()