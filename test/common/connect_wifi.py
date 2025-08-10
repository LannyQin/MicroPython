import network
from time import sleep,time

def connect_wifi(ssid,password,timeout=15,slcn=True):    #stop last and connect new
    wifi=network.WLAN(network.STA_IF)
    print(wifi.isconnected())
    if wifi.isconnected():
        if slcn:
            wifi.active(False)
        else:
            return wifi,2
    print('active')
    wifi.active(True)
    print('connect')
    wifi.connect(ssid,password)
    print('t0')
    t0=time()
    while True:
        if wifi.isconnected():
            return wifi,0
        if time() > t0+timeout:
            return wifi,1
        sleep(0.25)

if __name__ == '__main__':
    connect_wifi('Xiaomi_stream','1qazxsw20plmnko9')