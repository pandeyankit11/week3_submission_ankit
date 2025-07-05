import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class SecondPublisher(Node):
    def __init__(self):
        super().__init__('second_publisher')
        self.publisher = self.create_publisher(Int32, '/second', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.second = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.second
        self.publisher.publish(msg)
        self.get_logger().info(f'Published to /second: {self.second}')
        self.second += 1
        if self.second >= 60:
            self.second = 0

def main(args=None):
    rclpy.init(args=args)
    node = SecondPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
