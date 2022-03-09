# Write your code here :-)

# buzzer
# Det handler om å slå av og på pinne 0

from microbit import *

while True:
    pin0.write_digital(1)
    sleep(400)
    pin0.write_digital(0)
    sleep(400)

