from machine import Pin,SoftI2C,Timer

from libs.i2c_lcd import I2cLcd

i2c=SoftI2C(scl=Pin(25),sda=Pin(26),freq=1000000)

#获取I2C设备地址
address=i2c.scan()[0]

#定义I2cLcd对象
i2clcd=I2cLcd(i2c,address,2,16)

import network
import ntptime
from machine import RTC
from time import time,sleep_ms

from common.settings import Settings
# from common.wifi_manager import WifiManager

settings=Settings()
rtc=RTC()

# wifi=WifiManager(settings.ssid,settings.password,5,True)
# # wifi.disconnect()
# wifi.active(True)
# wifi.connect()
# print(wifi.ifconfig())

wifi=network.WLAN(network.STA_IF)
try:
    wifi.disconnect()
except:
    pass
wifi.active(True)
wifi.connect(settings.ssid,settings.password)
t0=time()
i2clcd.putstr('Connecting Wifi')
now=0
while True:
    now+=1
    if now%2==0:
        i2clcd.putstr('.')
    if time()>t0+10:
        i2clcd.putstr('Connection failed!')
        break
    elif wifi.isconnected():
        i2clcd.clear()
        i2clcd.putstr('Connected!      Sync time...')
        sleep_ms(300)
        try:
            ntptime.settime()
            i2clcd.clear()
            i2clcd.putstr('Suscess!')
            sleep_ms(300)
        except OSError:
            i2clcd.clear()
            i2clcd.putstr('OS Error!       Please restart!')
            sleep_ms(1000000000)
        break
    sleep_ms(100)

week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

def show_time(timer_obj):
    datetime=rtc.datetime()
    i2clcd.blink_cursor_off()
    i2clcd.hide_cursor()
    i2clcd.clear()
    i2clcd.putstr('%d-%02d-%02d   %s'%(datetime[0],datetime[1],datetime[2],week[datetime[3]]))
    i2clcd.putstr('    %02d:%02d:%02d'%(datetime[4]+8,datetime[5],datetime[6]))

i2clcd.clear()
show_time(None)

timer=Timer(0)
timer.init(mode=Timer.PERIODIC,period=1000,callback=show_time)