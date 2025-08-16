import network
from time import sleep

wifi = network.WLAN(network.STA_IF)
wifi.active(True)  # 观察是否还会触发复位
print("Wi-Fi 模块已激活")
# wifi.connect("SSID", "PASSWORD")  # 可后续再试
wifi.connect('Xiaomi_Stream','1qazxsw20plmnko9')
sleep(5)
print(wifi.isconnected())