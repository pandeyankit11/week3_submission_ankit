import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from kratos_ankit_interfaces.action import MoveArm
from rclpy.qos import QoSProfile
import time

class ArmActionServer(Node):
    def __init__(self):
        super().__init__('arm_action_server')
        self._server = ActionServer(
            self,
            MoveArm,
            'move_arm',
            self.execute_callback
        )
        self.current_angle = 0

    async def execute_callback(self, goal_handle):
        self.get_logger().info(f'Goal received: Move to {goal_handle.request.target_angle}°')
        feedback_msg = MoveArm.Feedback()

        while self.current_angle < goal_handle.request.target_angle:
            self.current_angle += 1
            feedback_msg.current_angle = self.current_angle
            self.get_logger().info(f'Current angle: {self.current_angle}°')
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()
        result = MoveArm.Result()
        result.result = f'Reached target angle: {self.current_angle}°'
        return result

def main(args=None):
    rclpy.init(args=args)
    node = ArmActionServer()
    rclpy.spin(node)
    rclpy.shutdown()
