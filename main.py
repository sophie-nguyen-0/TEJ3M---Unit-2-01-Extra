"""Example for Pico. Blinks the built-in LED."""
import time
import board
import digitalio

#variables
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# loop
while True:
    #turns on LED
    led.value = True
    #wait 1 second
    time.sleep(1)
    #turns LED off
    led.value = False
    time.sleep(1)