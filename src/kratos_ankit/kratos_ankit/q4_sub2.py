import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String

class ClockFormatter(Node):
    def __init__(self):
        super().__init__('clock_formatter')
        self.second = 0
        self.minute = 0
        self.hour = 0

        self.publisher = self.create_publisher(String, '/clock', 10)

        self.create_subscription(Int32, '/second', self.second_cb, 10)
        self.create_subscription(Int32, '/minute', self.minute_cb, 10)
        self.create_subscription(Int32, '/hour', self.hour_cb, 10)

    def second_cb(self, msg):
        self.second = msg.data
        self.publish_clock()

    def minute_cb(self, msg):
        self.minute = msg.data
        self.publish_clock()

    def hour_cb(self, msg):
        self.hour = msg.data
        self.publish_clock()

    def publish_clock(self):
        time_str = f"{self.hour:02}:{self.minute:02}:{self.second:02}"
        msg = String()
        msg.data = time_str
        self.publisher.publish(msg)
        self.get_logger().info(f'Published to /clock: {time_str}')

def main(args=None):
    rclpy.init(args=args)
    node = ClockFormatter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
