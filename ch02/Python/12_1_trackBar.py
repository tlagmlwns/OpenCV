import cv2
import numpy as np

def on_lc(pos):
    value = pos*16
    if value >= 255:
        value = 255
        
    img[:] = value
    cv2.imshow('image', img)
    
img = np.zeros((480, 640), np.uint8)

cv2.namedWindow('image', flags=cv2.WINDOW_NORMAL)
cv2.createTrackbar('level', 'image', 0, 16, on_lc)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()