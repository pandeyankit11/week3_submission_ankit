import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class HelloPublisher(Node):
    def __init__(self):
        super().__init__('hello_publisher')
        self.publisher_ = self.create_publisher(String, '/hello', 10)
        timer_period = 1.0 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter =0
    
    def timer_callback(self):
        msg = String()
        msg.data = "Hello World !"
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')
        self.counter += 1
        if self.counter >= 70:
            self.timer.cancel()

def main(args=None):
    rclpy.init(args=args)
    node = HelloPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()