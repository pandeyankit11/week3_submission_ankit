import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from kratos_ankit_interfaces.action import MoveArm

class ArmActionClient(Node):
    def __init__(self):
        super().__init__('arm_action_client')
        self._client = ActionClient(self, MoveArm, 'move_arm')

    def send_goal(self, angle):
        self._client.wait_for_server()
        goal_msg = MoveArm.Goal()
        goal_msg.target_angle = angle

        self._client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        ).add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected ❌')
            return

        self.get_logger().info('Goal accepted ✅')
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f"Feedback: Arm at {feedback_msg.feedback.current_angle}°")

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Result: {result.result}")

def main(args=None):
    rclpy.init(args=args)
    node = ArmActionClient()
    angle = int(input("Enter target angle: "))
    node.send_goal(angle)
    rclpy.spin(node)
    rclpy.shutdown()
