import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker():
  def __init__(self):
    self.pub = node.create_publisher(Int16, "countup", 10)
    self.n = 0
    node.create_timer(0.5, self.cb)

  def cb(self):
    msg = Int16()
    msg.data = self.n
    self.pub.publish(msg)
    self.n += 1

def main():
  rclpy.init()
  node = Node("Talker")
  talker = Talker(node)
  rclpy.spin(node)

if __name__ == '__main__':
  main()
