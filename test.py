from gpiozero import Motor
import time
from gpiostepper import Stepper

step_motor2 = Stepper(motor_pins=[6, 13, 19, 26], number_of_steps = 64, step_sequence = [[1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])

step_motor1 = Stepper(motor_pins=[14, 15, 18, 12], number_of_steps = 64, step_sequence = [[1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
# step_motor1 = Stepper(motor_pins=[14, 15, 18, 12], number_of_steps =64, step_sequence = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
step_motor1.set_speed(1500)
step_motor1.step(64*50)
step_motor1.step(-64*50)

step_motor2.set_speed(1500)
step_motor2.step(64*50)
step_motor2.step(-64*50)
