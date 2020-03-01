from gpiozero import LED
from time import sleep
import random

led = LED(25)
led2 = LED(24)

winner = random.randint(1,2)

'''
name = input("Enter your name: ")
if name == 'Sarah':
    delay = 0.5
elif name == "Bilal":
    delay = 0.05
elif name == "Rabab":
    delay = 1
else:
    delay = 3
'''
count = 10
delay = 0.1

while count > 0:
    led.on()
    led2.off()
    print("LED set to on")
    sleep(delay)

    led.off()
    led2.on()
    print('LED set to off')
    sleep(delay)

    count = count - 1

led.off()
led2.off()

if winner == 1:
    led.on()
else:
    led2.on()

