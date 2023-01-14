from gpiozero import Motor
import time
import keyboard
import sys, tty, termios
from gpiostepper import Stepper

front_left = Motor(27, 22, pwm=False)
front_right = Motor(3, 2, pwm=False)
back_left = Motor(24, 23, pwm=False)
back_right = Motor(16, 20, pwm=False)

left_arm = Stepper(motor_pins=[6, 13, 19, 26], number_of_steps = 64, step_sequence = [[1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
left_arm.set_speed(64*20)
right_arm = Stepper(motor_pins=[14, 15, 18, 12], number_of_steps = 64, step_sequence = [[1, 0, 0, 1], [1, 0, 0, 0], [1, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]])
right_arm.set_speed(64*20)

def all_forward(duration=0):
    front_left.forward()
    front_right.forward()
    back_left.forward()
    back_right.forward()
    time.sleep(duration)

def all_backward(duration=0):
    front_left.backward()
    front_right.backward()
    back_left.backward()
    back_right.backward()
    time.sleep(duration)

def turn_left(duration=0):
    front_left.backward()
    front_right.forward()
    back_left.backward()
    back_right.forward()
    time.sleep(duration)

def turn_right(duration=0):
    front_left.forward()
    front_right.backward()
    back_left.forward()
    back_right.backward()
    time.sleep(duration)

def all_right(duration=0):
    front_left.forward()
    front_right.backward()
    back_left.backward()
    back_right.forward()
    time.sleep(duration)    

def all_left(duration=0):
    front_left.backward()
    front_right.forward()
    back_left.forward()
    back_right.backward()  
    time.sleep(duration)

def just_dance():
    all_forward(1)
    all_backward(1)
    all_left(1)
    all_right(1)
    turn_right(0.5)
    turn_left(0.5)
    rotate_arm(right_arm, "clockwise", 64*10)
    rotate_arm(right_arm, "counter", 64*10)
    rotate_arm(left_arm, "clockwise", 64*10)
    rotate_arm(left_arm, "counter", 64*10)
    all_stop()

def wave_arm(arm):
    rotate_arm(arm, "clockwise", 64*50)
    rotate_arm(arm, "counter", 64*50)

def rotate_arm(arm, direction, steps=32):
    if direction == "clockwise":
        arm.step(steps)
    elif direction == "counter":
        arm.step(-steps)

def all_stop():
    front_left.stop()
    front_right.stop()
    back_left.stop()
    back_right.stop()

while True:
    print("waiting for goop...")

    keyboard_event = keyboard.read_event()
    key = "s"
    print(keyboard_event)
    if keyboard_event.event_type == keyboard.KEY_DOWN:
        key = keyboard_event.name
    
    print("you gave me this goop: " + key)
    if key == "q":
        all_stop()
        break
    elif key == "up":
        all_forward()
    elif key == "s":
        all_stop()
    elif key == "down":
        all_backward()
    elif key == "left":
        turn_left()
    elif key == "right":
        turn_right()
    elif key =="r":
        all_right()
    elif key == "l":
        all_left()   
    elif key == "d":
        just_dance()
    elif key == "p":
        wave_arm(right_arm)
    elif key == "o":
        wave_arm(left_arm)
    elif key == "y":
        rotate_arm(left_arm, "clockwise")
    elif key == "h":
        rotate_arm(left_arm, "counter")
    elif key == "u":
        rotate_arm(right_arm, "clockwise")
    elif key == "j":
        rotate_arm(right_arm, "counter")
print("Bring me some good goop next time")