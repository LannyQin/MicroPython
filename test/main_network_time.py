from machine import RTC
import ntptime

from common.connect_wifi import connect_wifi
from common.settings import Settings

#加载设置项
settings=Settings()

#尝试连接WiFi
wifi,wifi_status=connect_wifi(settings.ssid,settings.password)
# print(wifi.ifconfig(),wifi_status,wifi.config('mac'),wifi.config('essid'))
print(wifi_status)

#构建RTC时钟对象
rtc=RTC()
#如果Wifi已连接就同步时钟
if wifi_status==0 or wifi_status==2:
    try:
        ntptime.settime()
    except Exception as e:
        print(e.__class__,str(e))
#打印时间
print(rtc.datetime())