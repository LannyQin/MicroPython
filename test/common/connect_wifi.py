import network,ntptime
from machine import RTC
from time import sleep,time

def connect_wifi(ssid,password,timeout=15,slcn=True):    #stop last and connect new
    wifi=network.WLAN(network.STA_IF)
    if wifi.isconnected():
        if slcn:
            wifi.active(False)
        else:
            return wifi,2
    wifi.active(True)
    wifi.connect(ssid,password)
    t0=time()
    while True:
        if wifi.isconnected():
            return wifi,0
        if time() > t0+timeout:
            return wifi,1
        sleep(0.25)

def wlan_connected_only(func):
    def decorate(*args,**kwargs):
        wlan=network.WLAN(network.STA_IF)
        if wlan.isconnected():
            return func(*args,**kwargs)
        else:
            return 1
    return decorate

@wlan_connected_only
def settime(timezone=8):
    #构建RTC时钟对象
    rtc=RTC()
    try:
        ntptime.settime()
        datetime=list(rtc.datetime())
        datetime[4]+=timezone    #北京时间在+8时区
        rtc.datetime(datetime)
    except Exception as e:
        return e.__class__,str(e)

if __name__ == '__main__':
    connect_wifi('Xiaomi_stream','1qazxsw20plmnko9')