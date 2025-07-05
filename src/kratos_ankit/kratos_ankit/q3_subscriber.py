import rclpy
from rclpy.node import Node
from kratos_ankit_interfaces.msg import RoverStatus

class RoverStatusSubscriber(Node):
    def __init__(self):
        super().__init__('rover_status_subscriber')
        self.subscription = self.create_subscription(
            RoverStatus,
            'rover_status',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(
            f'Received RoverStatus:\n\n'
            f'  Velocity: {msg.velocity}\n\n'
            f'  Distance Traveled: {msg.distance}\n\n'
            f'  Coordinates: {msg.position}\n\n'
            f'  Battery Power Level: {msg.battery}\n\n'
            f'  Time of Travel: {msg.travel_time}\n\n\n'
        )

def main(args=None):
    rclpy.init(args=args)
    node = RoverStatusSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
