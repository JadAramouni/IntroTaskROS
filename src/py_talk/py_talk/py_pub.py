import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PyPublisher(Node):
    def __init__(self):
        super().__init__('py_publisher')
        self.pub = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(0.5, self.tick)
        self.count = 0

    def tick(self):
        msg = String()
        msg.data = f'Hello from ROS2 (Python)! #{self.count}'
        self.pub.publish(msg)
        self.get_logger().info(f'Published: "{msg.data}"')
        self.count += 1

def main():
    rclpy.init()
    node = PyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
