import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class S1Publisher(Node):
    def __init__(self):
        super().__init__('s1_publisher')
        self.publisher_ = self.create_publisher(String, '/s1', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)  # Publish every 1 second
        self.state = 'green'
        self.counter = 0

    def timer_callback(self):
        msg = String()
        msg.data = self.state
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published to /s1: {msg.data}')

        self.counter += 1
        if self.counter >= 10:
            self.state = 'red' if self.state == 'green' else 'green'
            self.counter = 0

def main(args=None):
    rclpy.init(args=args)
    node = S1Publisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
