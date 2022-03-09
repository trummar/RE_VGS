# Write your code here :-)

from microbit import *
# importere det som trengs av grunnleggende
# funksjoner

# husk at du kan sjekke dokumentasjonen på
# http://docs.micropython.org/en/latest/index.html#
# for å finne gyldige kommandoer og funksjoner.

# Kontrollere motor:

pin16.write_analog(770)   # = 75% 770/1023
pin8.write_analog(0)

pin14.write_analog(100)   # = 35% 360/1023
pin12.write_analog(0)

