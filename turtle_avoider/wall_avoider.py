import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class WallAvoider(Node):
	def __init__(self):
		super().__init__("wall_avoider")
		self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
		self.subscription = self.create_subscription(Pose, "/turtle1/pose", self.pose_callback, 10)
		
	def pose_callback(self, msg):
		twist = Twist()
		if msg.x < 1.0 or msg.x > 10.0 or msg.y < 1.0 or msg.y > 10.0:	
			twist.linear.x = 1.0
			twist.angular.z = 1.0
		else:
			twist.linear.x = 2.0
			twist.angular.z = 0.0
		self.publisher_.publish(twist)
		
def main(args=None):
	rclpy.init(args=args)
	node = WallAvoider()
	rclpy.spin(node)
	node.destroy_node()
	rclpy.shutdown()
	
if __name__ == "__main__":
	main()
