from machine import SoftI2C,Pin,RTC,Timer
from libs.ssd1306 import SSD1306_I2C
from time import sleep,time
import ntptime

from common.oled_show_character import *
from font.number_32 import number_32_dict
from common.connect_wifi import connect_wifi
from common.settings import Settings

i2c=SoftI2C(scl=Pin(22),sda=Pin(21))
print('scanning')
address=i2c.scan()[0]
print('scanned')

oled=SSD1306_I2C(128,64,i2c,address)

#加载设置项
settings=Settings()

week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

rtc=RTC()

#尝试连接WiFi
# wifi,wifi_status=connect_wifi(settings.ssid,settings.password)
# print(wifi.ifconfig(),wifi_status,wifi.config('mac'),wifi.config('essid'))
# 
# #构建RTC时钟对象
# #如果Wifi已连接就同步时钟
# if wifi_status==0 or wifi_status==2:
#     try:
#         ntptime.settime()
#     except Exception as e:
#         print(e.__class__,str(e))
#打印时间
print(rtc.datetime())

def print_time(timer_obj):
    datetime=rtc.datetime()
    format_date='%02d/%02d'%(datetime[1],datetime[2])
    format_date_list=[number_32_dict[character] for character in format_date]
    format_time='%02d:%02d:%02d'%(datetime[4],datetime[5],datetime[6])
    format_time_list=[number_32_dict[character] for character in format_time]
    show_characters(oled,format_date_list,0,0,32,16)
    show_characters(oled,format_time_list,0,32,32,16)
    oled.text(str(datetime[0]),88,6)
    oled.text(week[datetime[3]],92,16)
    oled.show()
    print(datetime[-2:])

timer=Timer(0)
timer.init(mode=Timer.PERIODIC,period=1000,callback=print_time)

# while True:
#     oled.fill(0)
#     oled.show()
#     sleep(1)
#     oled.fill(1)
#     oled.show()
#     sleep(1)
