#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray


class Test_Subscriber(Node):

    def __init__(self):
        super().__init__("test_sub")
        self.subscription = self.create_subscription(
            Float64MultiArray,
            'gps_data',
            self.listener_callback,
            10
        )

                
    def listener_callback(self, msg):
        self.get_logger().info('I heard: Lat: ' + str(msg.data[0]) + ', Lon: ' + str(msg.data[1]))

        

        
def main(args=None):
    rclpy.init(args=args)
    subscriber = Test_Subscriber()
    rclpy.spin(subscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()