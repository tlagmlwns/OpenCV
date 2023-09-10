import numpy as np
from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import *

cap = cv2.VideoCapture("../Videos/people.mp4")  # For Video

model = YOLO("../Yolo-Weights/yolov8l.pt")
