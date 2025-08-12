from machine import Pin,PWM,Timer,SoftI2C
from libs.ssd1306 import SSD1306_I2C
from font.number_32 import number_32_dict
from common.oled_show_character import show_characters

pin_out=Pin(26,Pin.OUT)
pwm=PWM(pin_out,freq=25000,duty=0)
pin_in=Pin(27,Pin.IN,Pin.PULL_DOWN)

i2c=SoftI2C(scl=Pin(22),sda=Pin(21))
print('scanning')
address=i2c.scan()[0]
print('scanned')

oled=SSD1306_I2C(128,64,i2c,address)
oled.fill(0)

duty=0
times=0
direction=1

def add_times(button):
    global times
    times+=1

def get_times(timer_object):
    global times
    print('speed:'+str(times*30))
    oled.fill(0)
    show_speed=str(times*30)
    show_speed_list=[number_32_dict[character] for character in show]
    show_characters(oled,show_speed_list,0,0,32,16)
    show_duty_list=[number_32_dict[character] for character in duty]
    show_characters(oled,show_duty_list,0,31,32,16)
    oled.show()
    times=0

def change_time(timer_object):
    global duty
    if duty>=1010:
        direction=0
    if duty<=10:
        diorection=1
    duty+=10*direction
    pwm.duty(duty)
    

pin_in.irq(add_times,Pin.IRQ_RISING)
timer=Timer(0)
timer.init(mode=Timer.PERIODIC,period=1000,callback=get_times)
timer_change_speed=Timer(1)
timer_change_speed.init(mode=Timer.PERIODIC,period=50,callback=change_time)