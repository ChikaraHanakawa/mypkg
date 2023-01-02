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
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImagePublisher():
  def __init__(self, node):
    super().__init__('image_publisher')
    self.pub = node.create_publisher(Image, 'video_frames', 10)
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.cap = cv2.VideoCapture(0)
    self.br = CvBridge()

  def timer_callback(self):
    dirname = 'face_images'

    ret, frame = self.cap.read()
    if ret == True:
      self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
    self.get_logger().info('Publishing video frame')

    '''cascade_filepath = "/home/chikara/ros2_ws/src/mypkg/mypkg/data/haarcascades/haarcascade_frontalface_alt.xml"
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
    cap.release() '''

def main(args=None):
  rclpy.init()
  image_publisher = ImagePublisher()
  rclpy.spin(image_publisher)
  image_publisher.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
