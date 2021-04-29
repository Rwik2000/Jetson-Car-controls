from adafruit_servokit import ServoKit
from adafruit_pca9685 import PCA9685
import busio
import time
from board import SCL, SDA

kit = ServoKit(channels=16)

for i in range(10):
    kit.servo[0].angle=90
    time.sleep(1)
    kit.servo[0].angle=60
    time.sleep(1)
    kit.servo[0].angle=98
    time.sleep(1)
    kit.servo[0].angle=120
    time.sleep(1)

kit.continuous_servo[1].throttle=1
time.sleep(3)