import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PySubscriber(Node):
    def __init__(self):
        super().__init__('py_subscriber')
        self.create_subscription(String, 'chatter', self.cb, 10)

    def cb(self, msg: String):
        self.get_logger().info(f'Received: "{msg.data}"')

def main():
    rclpy.init()
    node = PySubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
