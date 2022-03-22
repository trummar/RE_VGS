# Write your code here :-)

# Write your code here :-)
from microbit import *

streng = ""

# function to read data file:
def get_nv_data(name):
    try:
        with open(name) as f:
            v = int(f.read())
    except OSError:
        v = temperature()
        try:
            with open(name, 'w') as f:
                f.write(str(v))
        except OSError:
            display.scroll('Cannot create file %s' % name)

    except ValueError:
        display.scroll('invalid data in file %s' % name)
        v = temperature()

    return v

# function to write data file:
def set_nv_data(name, value):
    try:
        with open(name, 'w') as f:
            f.write(str(value))
    except OSError:
        display.scroll('Cannot write to file %s' % name)

min = get_nv_data('min.txt')
# max = get_nv_data('max.txt')

# while True:    # Må ha et endgame for å avslutte riktig
for i in range(20):
    currentTemp = temperature()

    streng = streng + str(currentTemp) + ","

    sleep(1000)
    # min = currentTemp

set_nv_data('min.txt', streng)

display.scroll("X")


