from machine import Pin
import time


a = Pin(19, Pin.OUT)
b = Pin(18, Pin.OUT)
c = Pin(5, Pin.OUT)
d = Pin(17, Pin.OUT)

a.value(0)
b.value(0)
c.value(0)
d.value(0)

delay_time_ms = 1


while True:
    a.value(1)
    b.value(0)
    c.value(0)
    d.value(0)
    time.sleep_ms(delay_time_ms)
    
    a.value(1)
    b.value(1)
    c.value(0)
    d.value(0)
    time.sleep_ms(delay_time_ms)
    
    a.value(0)
    b.value(1)
    c.value(0)
    d.value(0)
    time.sleep_ms(delay_time_ms)
    
    a.value(0)
    b.value(1)
    c.value(1)
    d.value(0)
    time.sleep_ms(delay_time_ms)
    
    a.value(0)
    b.value(0)
    c.value(1)
    d.value(0)
    time.sleep_ms(delay_time_ms)
    
    a.value(0)
    b.value(0)
    c.value(1)
    d.value(1)
    time.sleep_ms(delay_time_ms)
    
    a.value(0)
    b.value(0)
    c.value(0)
    d.value(1)
    time.sleep_ms(delay_time_ms)
    
    a.value(1)
    b.value(0)
    c.value(0)
    d.value(1)
    time.sleep_ms(delay_time_ms)