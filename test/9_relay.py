from machine import Pin,Timer
from time import sleep

relay=Pin(13,Pin.OUT)

up=True
sleep_time=0.1

def change_time(timer_obj):
    global up,sleep_time
    if up:
        if sleep_time>=1:
            up=False
        else:
            sleep_time+=0.01
    else:
        if sleep_time<=0.02:
            up=True
        else:
            sleep_time-=0.01

timer=Timer(0)
timer.init(mode=Timer.PERIODIC,period=50,callback=change_time)  

while True:
    relay.value(not relay.value())
    sleep(sleep_time)