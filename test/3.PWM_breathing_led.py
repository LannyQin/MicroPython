from machine import Pin,PWM
from time import sleep_ms

led=PWM(Pin(5,Pin.OUT),freq=1000,duty=512)

while True:
    for i in range(1024):
        led.duty(i)
        sleep_ms(1)
        print(led.duty())
    for i in range(1024):
        led.duty(1023-i)
        sleep_ms(1)
        print(led.duty())