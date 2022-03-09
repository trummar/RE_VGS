# Write your code here :-)

from microbit import *
import neopixel as pixel
# from random import randint

visled = pixel.NeoPixel(pin13,12)

visled[4] = (40, 0, 40)

visled.show()





