#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# © 2022 Chikara Hanakawa                                                                                                                                                                              
# SPDX-FileCopyrightText: 2022 Chikara Hanakawa
# SPDX-License-Identifier: BSD-3-Clause
 
import cv2 
import os
import numpy as np
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

class detectorimages(Node):
  def __init__(self):
    self.pub = node.create_publisher(Float64MultiArray, 'detector', 10)
    detector_period = 0.5
    self.detector = self.create_detector(timer_period, self.detector_callback)
    self.i = 0

  def detector_callback(self):
    msg = FloatMultiArray()
    self.publisher_.publish(msg)

    dirname = 'face_images'
                
    cap = cv2.VideoCapture(0)
                
    cascade_filepath = "/home/chikara/ros2_ws/src/mypkg/mypkg/data/haarcascades/haarcascade_frontalface_alt.xml"
    FaceCascade = cv2.CascadeClassifier(cascade_filepath)
                
    count = 0   
                
    while True:
      ret, frame = cap.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      Face = FaceCascade.detectMultiScale(gray,1.1,3,minSize=(100,100))
      msg = Face
      if not os.path.exists(dirname):
        os.mkdir(dirname)
                
      for (x,y,w,h) in Face:
        count += 1
        count_padded = '%05d' % count
        cv2.rectangle(frame, (x,y),(x+w,y+h),(255,0,0),thickness=2)
        write_file = count_padded + ".png"
        cv2.imwrite(os.path.join(dirname, write_file), frame)
                
      cv2.imshow('result', frame)
                
      key = cv2.waitKey(1)
      if key != -1: 
        break  
                
    cv2.destroyAllWindows()
    cap.release() 

def main(args=None):
  rclpy.init(args=args)
  detectorpublisher = detectorimages()
  rclpy.spin()
  detectorimages.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
