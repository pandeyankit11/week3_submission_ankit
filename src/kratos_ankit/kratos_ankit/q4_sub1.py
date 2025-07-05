import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SecondSubscriber(Node):
    def __init__(self):
        super().__init__('second_subscriber')
        self.subscription = self.create_subscription(Int32, '/second', self.callback, 10)

    def callback(self, msg):
        self.get_logger().info(f'Received second: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = SecondSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
