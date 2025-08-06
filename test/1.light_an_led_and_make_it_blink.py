from machine import Pin
from time import sleep

led_pin=Pin(14,Pin.OUT)

led_pin.off()

for i in range(6):
    led_pin.value(not led_pin.value())
    sleep(1)