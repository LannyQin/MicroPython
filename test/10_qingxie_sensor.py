from machine import Pin
from time import sleep_ms

light=Pin(2,Pin.OUT)
sensor=Pin(26,Pin.IN,Pin.PULL_DOWN)

while True:
    light.value(not sensor.value())
    sleep_ms(20)