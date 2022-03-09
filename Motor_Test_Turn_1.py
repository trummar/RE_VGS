# Write your code here :-)

from microbit import *

# importere det som trengs grunnleggende

# husk at du kan sjekke dokumentasjonen på
# http://docs.micropython.org/en/latest/index.html#
# for å finne gyldige kommandoer og funksjoner.

# Kontrollere motor:

pin16.write_digital(1)  # Venstre motor
pin8.write_digital(0)

pin14.write_digital(1)  # Høyre motor
pin12.write_digital(0)

sleep(1000)

pin14.write_digital(0)  # Høyre motor
pin12.write_digital(0)

sleep(1000)

pin16.write_digital(1)  # Venstre motor
pin8.write_digital(0)

pin14.write_digital(1)  # Høyre motor
pin12.write_digital(0)

sleep(1000)

# motor off
pin16.write_digital(0)
pin8.write_digital(0)
pin14.write_digital(0)
pin12.write_digital(0)
