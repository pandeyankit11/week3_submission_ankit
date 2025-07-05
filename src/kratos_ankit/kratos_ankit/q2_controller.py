import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class S2Controller(Node):
    def __init__(self):
        super().__init__('s2_controller')
        self.subscriber = self.create_subscription(String, '/s1', self.s1_callback, 10)
        self.publisher = self.create_publisher(String, '/s2', 10)

    def s1_callback(self, msg):
        s2_msg = String()
        if msg.data == 'green':
            s2_msg.data = 'red'
        elif msg.data == 'red':
            s2_msg.data = 'green'
        else:
            s2_msg.data = 'unknown'

        self.publisher.publish(s2_msg)
        self.get_logger().info(f'Received from /s1: {msg.data} → Published to /s2: {s2_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = S2Controller()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
