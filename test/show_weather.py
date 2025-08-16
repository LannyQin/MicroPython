from machine import Pin,SoftI2C,RTC,Timer
from libs.ssd1306_1 import SSD1306_I2C
from common.settings import Settings
from common.get_weather import get_weather
from common.oled_show_character import show_characters
from common.connect_wifi import settime
from font.number_32 import number_32_dict
from libs import ufont

i2c=SoftI2C(sda=Pin(21),scl=Pin(22))
address=i2c.scan()[0]
oled=SSD1306_I2C(128,64,i2c,address)

settings=Settings()
rtc=RTC()
week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
week_zh=['周一','周二','周三','周四','周五','周六','周日']

font = ufont.BMFont("font/dengxian12.bmf")
oled.fill(0)
# font.text(oled, "", 0, 0, show=True,auto_wrap=True)

def check_weather(timer_obj):
    global weather,future_weather,check_time,checking
    checking=True
    oled.fill(0)
    font.text(oled,'查询天气中...',22,26)
    result=get_weather(settings.city,settings.key)
    if result != 1:
        weather,future_weather=result[0],result[1]
    else:
        raise NameError    #瞎写的
    t=rtc.datetime()
    check_time='%02d:%02d'%(t[4],t[5])
    checking=False

try:
    check_weather(None)
except NameError:
    oled.fill(0)
    font.text(oled,'未连接网络！',28,26)
    raise SystemExit


def show_weather(timer_obj):
    if not checking:
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

def show_weather_2(timer_obj):
    if not checking:
        t=rtc.datetime()
        oled.fill(0)
        time='%02d:%02d:%02d'%(t[4],t[5],t[6])
        time_list=[number_32_dict[character] for character in time]
        show_characters(oled,time_list,0,0,32,16)
        font.text(oled,'%04d/%02d/%02d%s'%(t[0],t[1],t[2],week_zh[t[3]]),0,28,show=False)
        font.text(oled,'%s  %02dC  %02d'%(weather.info,weather.temperature,weather.humidity)+'%',0,40,show=False)
        font.text(oled,'%s%s 空气指数%d'%(weather.direct,weather.power,weather.aqi),0,52,show=False)
        font.text(oled,'更新于',92,28,show=False)
        font.text(oled,'%s'%check_time,97,40)

def _settime(timer_obj):
    settime()

show_timer=Timer(1)
show_timer.init(mode=Timer.PERIODIC,period=1000,callback=show_weather_2)
check_timer=Timer(2)
check_timer.init(mode=Timer.PERIODIC,period=1800000,callback=check_weather)
settime_timer=Timer(3)
settime_timer.init(mode=Timer.PERIODIC,period=600000,callback=_settime)