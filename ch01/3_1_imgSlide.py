import os
import sys
import glob
import cv2
img_files = glob.glob('.\\like\\*.jpg')

if not img_files:
    print("There are no jpg files in 'image' folder")
    sys.exit()
    
cv2.namedWindow("image", cv2.WINDOW_NORMAL) #화면 창 조절
cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, 
                        cv2.WINDOW_FULLSCREEN) #화면 풀스크린
cnt = len(img_files)
idx = 0
while True:
    img = cv2.imread(img_files[idx])
    if img is None:
        print("Image load failed!")
        break
    cv2.imshow("image", img)
    if cv2.waitKey(1000) >= 0:
        break
    idx+=1
    if idx>=cnt:
        idx=0
cv2.destroyAllWindows()