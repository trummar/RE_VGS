# Write your code here :-)

from microbit import *
# import neopixel

rightVal = pin1.read_analog()

# leftVal = str(pin2.read_analog())



display.scroll(rightVal, delay = 400)
