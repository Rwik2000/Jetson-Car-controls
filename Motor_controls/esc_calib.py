import adafruit_pca9685
import busio
from board import SCL, SDA
import time
from adafruit_motor import servo
i2c = busio.I2C(SCL, SDA)
pwm = adafruit_pca9685.PCA9685(i2c)

pwm.frequency =60
esc = servo.ContinuousServo(pwm.channels[1], min_pulse=1000, max_pulse=2000)
# esc.set_pulse_width_range(1000,2000)
esc.throttle = 1

input("connect power and press ENTER")
esc.throttle = 0
input("neutral")
time.sleep(1)
esc.throttle = 1
input("max")
time.sleep(1)
esc.throttle = -1
input("min")
time.sleep(1)


esc.throttle = 0.07
time.sleep(1)
esc.throttle=-1
pwm.deinit()
