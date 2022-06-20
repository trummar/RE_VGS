# Write your code here :-)

from microbit import *
import radio
radio.config(group=73)
radio.on()

while True:
    message = radio.receive()
    sleep(20)
    # print(message)

    if message is not None:
        print(message)

    # lag if system for å styre noe.
    # eller bruke display.scroll(
