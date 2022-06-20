# Write your code here :-)

from microbit import *
from utime import ticks_us, sleep_us

SONAR = pin15
# NO_PULL = 0

def sonar():
    SONAR.write_digital(1)  # Send 10us Ping pulse
    sleep_us(10)
    SONAR.write_digital(0)
    SONAR.set_pull(SONAR.NO_PULL)
    while SONAR.read_digital() == 0:  # ensure Ping pulse has cleared
        pass
    start = ticks_us()   # define starting time
    while SONAR.read_digital() == 1:   # wait for Echo pulse to return
        pass
    end = ticks_us()   # define ending time
    echo = end-start
    distance = int(0.01715 * echo)   # Calculate cm distance
    return distance

while True:
    vis = sonar()
    display.scroll(vis)   # Innefor denne løkka kan du bygge noe flott
    sleep(1000)







