# Write your code here :-)
from microbit import *

drive = 1

# left forward
def motor_lf():
    pin16.write_digital(1)
    pin8.write_digital(0)


def motor_lb():  # left backward
    pin16.write_digital(0)
    pin8.write_digital(1)


def motor_rf():  # right forward
    pin14.write_digital(1)
    pin12.write_digital(0)


def motor_rb():  # right backward
    pin14.write_digital(0)
    pin12.write_digital(1)


def motor_off():
    pin16.write_digital(0)
    pin8.write_digital(0)
    pin14.write_digital(0)
    pin12.write_digital(0)


while drive == 1:  # Kan være "True" også, altså while True
    if button_a.is_pressed():
        motor_lf()
        motor_rf()
    elif button_b.is_pressed():
        motor_off()
    else:
        # display.scroll("X")
        pass
