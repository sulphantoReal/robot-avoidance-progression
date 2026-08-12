import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan

class ObstacleAvoider(Node):
    def __init__(self):
        super().__init__("obstacle_avoider")
        self.publisher_ = self.create_publisher(Twist, "/cmd_vel", 10)
        self.subscription = self.create_subscription(LaserScan, "/scan", self.scan_callback, 10)

    def scan_callback(self, msg):
        front_ranges = msg.ranges[0:15] + msg.ranges[-15:]
        valid_ranges = [r for r in front_ranges if r > 0.0]

        twist = Twist()
        if valid_ranges and min(valid_ranges) < 0.5:
            twist.linear.x = 0.0
            twist.angular.z = 0.5
        else:
            twist.linear.x = 0.15
            twist.angular.z = 0.0
        self.publisher_.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoider()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
