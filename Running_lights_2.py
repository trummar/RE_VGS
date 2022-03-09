# Write your code here :-)

from microbit import *
import neopixel
from random import randint

fireleds = neopixel.NeoPixel(pin13,12)

# fireleds[1] = (40, 0, 40)

while True:
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    for i in range(12):
        fireleds[i] = (r, g, b)
        fireleds.show()
        sleep(100)
    for i in range(12):
        fireleds[i] = (0, 0, 0)
        fireleds.show()
        sleep(100)
