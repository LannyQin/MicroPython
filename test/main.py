from machine import RTC
import webrepl

from common.connect_wifi import connect_wifi,settime
from common.settings import Settings

#加载设置项
settings=Settings()

#尝试连接WiFi
connect_wifi(settings.ssid,settings.password)
# print(wifi.ifconfig(),wifi_status,wifi.config('mac'),wifi.config('essid'))

webrepl.start()

rtc=RTC()
settime()

#打印时间
print(rtc.datetime())

import show_weather
