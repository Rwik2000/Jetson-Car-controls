from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=16, frequency=50)

kit.continuous_servo[1].set_pulse_width_range(1000,2000)
time.sleep(1)
kit.continuous_servo[1].throttle = 1
time.sleep(0.5)
kit.continuous_servo[1].throttle = -1
time.sleep(0.5)
kit.continuous_servo[1].throttle = 0
time.sleep(0.5)



# for i in range(10):
#     kit.servo[0].angle=90
#     time.sleep(1)
#     kit.servo[0].angle=60
#     time.sleep(1)
#     kit.servo[0].angle=90
#     time.sleep(1)
#     kit.servo[0].angle=120
#     time.sleep(1)

# kit.continuous_servo[1].throttle=1
# time.sleep(3)