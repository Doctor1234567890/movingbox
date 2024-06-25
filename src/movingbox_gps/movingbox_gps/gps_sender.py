#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from gps3 import gps3

class GPS_Sender(Node):

    def __init__(self):
        super().__init__("gps_sender")
        self.get_logger().info("hi.")
        gps_socket = gps3.GPSDSocket()
        data_stream = gps3.DataStream()
        gps_socket.connect()
        gps_socket.watch()
        
        for new_data in gps_socket:
            if new_data:
                data_stream.unpack(new_data)
                self.get_logger().info('Altitude = ' + str(data_stream.TPV['alt']))
                self.get_logger().info('Latitude = ' + str(data_stream.TPV['lat']))
                self.get_logger().info('Longitude = ' + str(data_stream.TPV['lon']))
                


        
def main(args=None):
    rclpy.init(args=args)
    sender = GPS_Sender()
    rclpy.shutdown()

if __name__ == '__main__':
    main()