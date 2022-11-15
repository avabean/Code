from gpiozero import Motor
import time
import keyboard

front_left = Motor(27, 22, pwm=False)
front_right = Motor(3, 2, pwm=False)
back_left = Motor(24, 23, pwm=False)
back_right = Motor(16, 20, pwm=False)

def all_forward():
    front_left.forward()
    front_right.forward()
    back_left.forward()
    back_right.forward()
    
def all_backward():
    front_left.backward()
    front_right.backward()
    back_left.backward()
    back_right.backward()

def turn_left():
    front_left.backward()
    front_right.forward()
    back_left.backward()
    back_right.forward()

def turn_right():
    front_left.forward()
    front_right.backward()
    back_left.forward()
    back_right.backward()

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

print("Bring me some good goop next time")