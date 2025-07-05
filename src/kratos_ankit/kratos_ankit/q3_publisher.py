import rclpy
from rclpy.node import Node
from kratos_ankit_interfaces.msg import RoverStatus
from geometry_msgs.msg import Twist, Pose
from std_msgs.msg import Float32
from builtin_interfaces.msg import Time

class RoverStatusPublisher(Node):
    def __init__(self):
        super().__init__('rover_status_publisher')
        self.publisher_ = self.create_publisher(RoverStatus, 'rover_status', 10)
        self.timer = self.create_timer(1.0, self.publish_status) # 1 Hz

    def publish_status(self):
        msg = RoverStatus()
        msg.velocity = Twist()
        msg.position = Pose()
        msg.distance = Float32(data=123.4)
        msg.battery = Float32(data=78.9)
        msg.travel_time = Time(sec=456, nanosec=700000000)
        self.publisher_.publish(msg)
        self.get_logger().info('Published RoverStatus message')

def main(args=None):
    rclpy.init(args=args)
    node = RoverStatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
