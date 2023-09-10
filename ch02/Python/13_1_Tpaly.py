import sys
import numpy as np
import cv2
import random

cap1 = cv2.VideoCapture("C:\shj\OpenCV\opencv\ch02\q.mp4")
cap2 = cv2.VideoCapture("C:\shj\OpenCV\opencv\ch02\q2.mp4")

if not cap1.isOpened() or not cap2.isOpened():
    print("video open failed!")
    sys.exit()
    
# 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)

print("frame_cnt1:", frame_cnt1)
print("frame_cnt2:", frame_cnt2)
print("FPS:", fps)

fps2 = cap2.get(cv2.CAP_PROP_FPS)
print("fps2:", fps2)

delay = int(1000 / fps)
print("delay:", delay)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"DIVX")

# 출력 동영상 객체 생성
out = cv2.VideoWriter("output.avi", fourcc, fps, (w, h))

# 1번 동영상 복사
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()
    if not ret1:
        print("frame read error!")
        sys.exit()
    out.write(frame1)
    print(".", end="")
    cv2.imshow("output", frame1)
    cv2.waitKey(delay)

for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    if not ret1 or not ret2:
        print("frame read error!")
        sys.exit()
    dx = int(w / effect_frames) * i
    frame = np.zeros((h, w, 3), dtype=np.uint8)
    #frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    #frame[:, dx:w, :] = frame1[:, dx:w, :]
    #alpha = i / effect_frames
    #frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)
    
    #dx = int(w / effect_frames) * i
    #dy = int(h / effect_frames) * i
    #frame = np.zeros((h, w, 3), dtype=np.uint8)
    #frame[0:dy, 0:dx, :] = frame2[0:dy, 0:dx, :]
    #frame[dy:h, dx:w, :] = frame1[dy:h, dx:w, :]

    alpha = i / effect_frames
    if alpha < 0.5:
        frame = cv2.flip(frame1, 1)  # frame1을 좌우로 미러링
    else:
        frame = cv2.flip(frame2, 1)  # frame2를 좌우로 미러링
       
    out.write(frame)
    print(".", end="")
    cv2.imshow("output", frame)
    cv2.waitKey(delay)

# 2번 동영상을 복사
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()
    if not ret2:
        print("frame read error!")
        sys.exit()
    out.write(frame2)
    print(".", end="")
    cv2.imshow("output", frame2)
    cv2.waitKey(delay)

print("\noutput.avi file is successfully generated!")

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
