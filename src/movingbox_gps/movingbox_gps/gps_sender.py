#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray

from gps3 import gps3

class GPS_Sender(Node):

    def __init__(self):
        super().__init__("gps_sender")

        self.gps_socket = gps3.GPSDSocket()
        self.data_stream = gps3.DataStream()
        self.gps_socket.connect()
        self.gps_socket.watch()

        self.create_timer(1, self.timer_callback)
        self.publisher = self.create_publisher(Float64MultiArray, "/gps_sender", 10)
                
    def timer_callback(self):
        new_data = self.gps_socket.next()
        if not new_data: return

        self.data_stream.unpack(new_data)
        logger = self.get_logger()

        msg = Float64MultiArray()
        lat = self.data_stream.TPV['lat']
        lon = self.data_stream.TPV['lon']
        if lat == "n/a" or lon == "n/a": return logger.info("No data")

        msg.data = [float(lat), float(lon)]
        self.publisher.publish(msg)

        
def main(args=None):
    rclpy.init(args=args)
    sender = GPS_Sender()
    rclpy.spin(sender)
    rclpy.shutdown()

if __name__ == '__main__':
    main()