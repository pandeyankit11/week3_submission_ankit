import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MinuteHourPublisher(Node):
    def __init__(self):
        super().__init__('minute_hour_publisher')
        self.minute_pub = self.create_publisher(Int32, '/minute', 10)
        self.hour_pub = self.create_publisher(Int32, '/hour', 10)
        self.second_sub = self.create_subscription(Int32, '/second', self.second_callback, 10)

        self.minute = 0
        self.hour = 0

    def second_callback(self, msg):
        if msg.data == 0:
            self.minute += 1
            if self.minute >= 60:
                self.minute = 0
                self.hour += 1

            min_msg = Int32()
            min_msg.data = self.minute
            self.minute_pub.publish(min_msg)
            self.get_logger().info(f'Published to /minute: {self.minute}')

            hr_msg = Int32()
            hr_msg.data = self.hour
            self.hour_pub.publish(hr_msg)
            self.get_logger().info(f'Published to /hour: {self.hour}')

def main(args=None):
    rclpy.init(args=args)
    node = MinuteHourPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
