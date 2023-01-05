# © 2022 Chikara Hanakawa
# SPDX-FileCopyrightText: 2022 Chikara Hanakawa
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import numpy as np

dirname = 'face_images'
cascade_filepath = "/home/chikara/ros2_ws/src/mypkg/mypkg/data/haarcascades/haarcascade_frontalface_alt2.xml"
FaceCascade = cv2.CascadeClassifier(cascade_filepath)
count = 0

def mosaic(img, alpha):
  w = img.shape[1]
  h = img.shape[0]
  img = cv2.resize(img, (int(w*alpha), int(h*alpha)))
  img = cv2.resize(img, (w, h), interpolation=cv2.INTER_NEAREST)
  return img 

class ImageSubscriber(Node):
  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(
      Image, 
      'video_frames',
      self.listener_callback,
      10)
    self.subscription
    self.br = CvBridge()

  def listener_callback(self, data):
    global count
    self.get_logger().info('Receiving video frame')
    current_frame = self.br.imgmsg_to_cv2(data)
    gray = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)
    Face = FaceCascade.detectMultiScale(gray,1.1,3,minSize=(100,100))
    if not os.path.exists(dirname):
      os.mkdir(dirname)
    if len(Face) > 0:
      for (x, y, w, h) in Face:
        current_frame[y:y+h, x:x+w] = mosaic(current_frame[y:y+h, x:x+w], 0.07)
        count_padded = '%05d' % count
        write_file = count_padded + ".png"
        cv2.imwrite(os.path.join(dirname, write_file), current_frame)
        count += 1

    cv2.imshow("camera", current_frame)
    cv2.waitKey(1)

def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
