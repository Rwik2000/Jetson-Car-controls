import adafruit_pca9685
import busio
from board import SCL, SDA
import time
from adafruit_motor import servo
# from adafruit_servokit import ServoKit

i2c = busio.I2C(SCL, SDA)
pwm = adafruit_pca9685.PCA9685(i2c)

pwm.frequency =60
esc = servo.ContinuousServo(pwm.channels[1], min_pulse=1000, max_pulse=2000)
steer = servo.Servo(pwm.channels[0])
# esc.set_pulse_width_range(1000,2000)
# esc.throttle = 1

st = time.time()
while time.time() - st < 1.5:
    steer.angle = 90
    esc.throttle = 0.3
esc.throttle = -1
steer.angle = 90

 #0.075 threshold
# time.sleep(5)
# esc.throttle = -1
pwm.deinit()
