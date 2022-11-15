from gpiozero import Motor
import time

motor = Motor(27, 22, pwm=False)

motor.forward()
time.sleep(1)

motor.backward()
time.sleep(1)

motor.stop()
