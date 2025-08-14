import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class HelloSubscriber(Node):
    def __init__(self):
        super().__init__('hello_subscriber')
        self.publisher = self.create_publisher(String, '/helloworld', 10)
        self.subscription = self.create_subscription(String, '/hello', self.listener_callback, 10)

        self.last_received_time = 0.0  
        self.timer = self.create_timer(0.5, self.timer_callback)  
        

    def listener_callback(self, msg):
    
        self.last_received_time = time.time()
        
        self.publisher.publish(msg)
        self.get_logger().info(f'Forwarded: {msg.data}')

    def timer_callback(self):
    
        if time.time() - self.last_received_time > 3.0:
            zero_msg = String()
            zero_msg.data = "0"
            self.publisher.publish(zero_msg)
            
            

def main(args=None):
    rclpy.init(args=args)
    node = HelloSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
