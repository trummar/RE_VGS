# Write your code here :-)

from microbit import *
import radio
radio.config(group=73)
radio.on()
# t = 0
# v = (t,0,0)

while True:
    sleep(1000)

    t = temperature()
    # t_string = str(t)
    v = (t, 0, 0)

    # radio.send(str(accelerometer.get_values()))
    radio.send(str(v))
    # radio.send(str(temperature()))
