import matplotlib.pyplot as plt
import cv2

imgBGR1 = cv2.imread('C:\shj\OpenCV\opencv\ch01\like\dog4.jpg')
imgRGB1 = cv2.cvtColor(imgBGR1, cv2.COLOR_BGR2RGB)
imgGray1 = cv2.imread('C:\shj\OpenCV\opencv\ch01\like\dog4.jpg',cv2.IMREAD_GRAYSCALE)
imgBGR2 = cv2.imread('C:\shj\OpenCV\opencv\ch01\like\dog1.jpg')
imgRGB2 = cv2.cvtColor(imgBGR2, cv2.COLOR_BGR2RGB)
imgGray2 = cv2.imread('C:\shj\OpenCV\opencv\ch01\like\dog1.jpg',cv2.IMREAD_GRAYSCALE)

plt.subplot(221), plt.axis('off'), plt.imshow(imgRGB1)
plt.subplot(222), plt.axis('off'), plt.imshow(imgGray1, cmap='gray')
plt.subplot(223), plt.axis('off'), plt.imshow(imgRGB2)
plt.subplot(224), plt.axis('off'), plt.imshow(imgGray2, cmap='gray')
plt.show()