from machine import Pin,SoftI2C,RTC,Timer
from libs.ssd1306_1 import SSD1306_I2C
from common.settings import Settings
from common.get_weather import get_weather
import ufont

i2c=SoftI2C(sda=Pin(21),scl=Pin(22))
address=i2c.scan()[0]
oled=SSD1306_I2C(128,64,i2c,address)

settings=Settings()
rtc=RTC()
week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

font = ufont.BMFont("font/dengxian12.bmf")
oled.fill(0)
# font.text(oled, "", 0, 0, show=True,auto_wrap=True)

def check_weather():
    global weather,future_weather,check_time
    oled.fill(0)
    font.text(oled,'查询天气中...',22,26)
    weather,future_weather=get_weather(settings.city,settings.key)
    t=rtc.datetime()
    check_time='%02d:%02d'%(t[4],t[5])

check_weather()


def show_weather(timer_obj):
    t=rtc.datetime()
    oled.fill(0)
    oled.text('%04d/%02d/%02d'%(t[0],t[1],t[2]),0,0)
    oled.text('%02d:%02d:%02d %s'%(t[4],t[5],t[6],week[t[3]]),0,8)
    font.text(oled,'天气:%s'%weather.info,0,16,show=False)
    font.text(oled,'温度/湿度:%02dC/%02d'%(weather.temperature,weather.humidity)+'%',0,28,show=False)
    font.text(oled,'%s:%s'%(weather.direct,weather.power),0,40,show=False)
    font.text(oled,'空气指数:%d'%weather.aqi,0,52,show=False)
    font.text(oled,'更新于',91,40,show=False)
    font.text(oled,check_time,95,52,show=False)
    oled.show()
    
show_timer=Timer(1)
show_timer.init(mode=Timer.PERIODIC,period=1000,callback=show_weather)
check_timer=Timer(2)
check_timer.init(mode=Timer.PERIODIC,period=1800000,callback=check_weather)