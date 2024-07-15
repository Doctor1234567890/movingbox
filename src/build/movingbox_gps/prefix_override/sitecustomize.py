import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/movingbox/ros2_ws/src/install/movingbox_gps'
