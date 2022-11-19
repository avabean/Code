from gpiozero import Motor
import time
import keyboard
import sys, tty, termios

front_left = Motor(27, 22, pwm=False)
front_right = Motor(3, 2, pwm=False)
back_left = Motor(24, 23, pwm=False)
back_right = Motor(16, 20, pwm=False)

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
    all_stop()

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

print("Bring me some good goop next time")