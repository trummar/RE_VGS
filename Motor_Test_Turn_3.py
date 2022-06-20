# Write your code here :-)
from microbit import *

def forward_left():
    pin16.write_digital(1)  # Venstre motor
    pin8.write_digital(0)

def forward_right():
    pin14.write_digital(1)  # Høyre motor
    pin12.write_digital(0)

def fremover():
    forward_left()
    forward_right()

def stop():
    pin16.write_digital(0)  # Venstre motor
    pin8.write_digital(0)
    pin14.write_digital(0)  # Høyre motor
    pin12.write_digital(0)

def right():
    pin16.write_digital(1)  # Venstre motor
    pin8.write_digital(0)
    sleep(500)
    pin16.write_digital(0)  # Venstre motor
    pin8.write_digital(0)

def left():
    pin14.write_digital(1)  # Høyre motor
    pin12.write_digital(0)
    sleep(500)
    pin14.write_digital(0)  # Høyre motor
    pin12.write_digital(0)

fremover()  # Her starter programmet
sleep(1500)
right()
stop()

