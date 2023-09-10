import os
import sys
import glob
import cv2
img1 = cv2.imread('opencv\ch02\cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('opencv\ch02\cat.bmp', cv2.IMREAD_COLOR)


h, w = img2.shape[:2]

#1 - 느린 for 문
# for y in range(h):
#     for x in range(w):
#         img1[y, x] = 255
#         img2[y, x] = [0, 0, 255]
        
#2 - 답
#img1[:,:] = 255
#img2[:,:] = (0,0,255)

img1[10:50, 250:350] = 0
img2[100:200, 250:350] = (0,0,255)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey()
cv2.destroyAllWindows()
