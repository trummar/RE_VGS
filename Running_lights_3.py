# Write your code here :-)

from microbit import *
import neopixel
from random import randint

visled = neopixel.NeoPixel(pin13, 12)

# visled[4] = (40, 0, 40)   # r,g,b 0-255

while True:
    for i in range(12):
        #  Hvis man flytter def av
        #  r,g,b inn her vil det forandres
        #  ganske mye

        # ToDo!!!!!!!!!
        # Må vise noen leds her
        # Må/bør bruke variabelen i
        # for å variere eller telle
        visled[4] = (40, 0, 40)   # r,g,b 0-255

        visled.show()     # Vise led
        sleep(100)          # "sove" 0.1 s

    for i in range(12):
        visled[i] = (0, 0, 0)     # slå av led
        visled.show()             # make it so
        sleep(100)

