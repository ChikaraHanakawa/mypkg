#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import sys
import numpy as np

cap = cv2.VideoCapture(0)

#if cap.isOpend() is False:
  #sys.exit("can not open camera")

cascade_filepath = "/home/chikara/ros2_ws/src/mypkg/mypkg/data/haarcascades/haarcascade_frontalface_alt.xml"
FaceCascade = cv2.CascadeClassifier(cascade_filepath)

while True:
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  Face = FaceCascade.detectMultiScale(gray,1.1,3,minSize=(100,100))
  for (x,y,w,h) in Face:
    cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),thickness=2)

  cv2.imshow('result', frame)
  key = cv2.waitKey(1)
  if key != -1:
    break

cv2.destroyAllWindows()
cap.release()
