import sys
import cv2

print('Hello OpenCV', cv2.__version__)

#img = cv2.imread('cat.bmp')
img = cv2.imread('C:\shj\OpenCV\opencv\ch01\like\dog4.jpg')
if img is None:
    print('Image load failed')
    sys.exit()

cv2.namedWindow('image', flags=cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()