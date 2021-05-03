import math
import time
import cv2
import numpy as np
import pyrealsense2 as rs

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()

config.enable_stream(rs.stream.color,640, 360,rs.format.bgr8, 30)

# Start streaming
pipeline.start(config)

while True:
    st = time.time()
    frames = pipeline.wait_for_frames()

    color_frame = frames.get_color_frame()

    color_image = np.asanyarray(color_frame.get_data())
    # color_image = cv2.resize(color_image,(640,320))
    cv2.imshow("color", color_image)
    print(time.time()- st)
    color_image = cv2.cvtColor(color_image,cv2.COLOR_BGR2HSV)
    color_image = cv2.inRange(color_image,(18,20,120),(25,180,200))
    cv2.imshow("thresh", color_image)
    cv2.waitKey(1)
    print(time.time()- st)
    print('-----------------------------------------')

    