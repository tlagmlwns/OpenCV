import cv2
img1 = cv2.imread('opencv\ch02\cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('opencv\ch02\cat.bmp', cv2.IMREAD_COLOR)

print("type(img1): ", type(img1))
print("img1.shape: ", img1.shape)
print("img2.shape: ", img2.shape)
print("img2.dtype: ", img2.dtype)

h, w = img2.shape[:2]
print('img2 size: {} X {}'.format(w, h))
if len(img1.shape) == 2:
    print('lmg1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey()

cv2.destroyAllWindows()