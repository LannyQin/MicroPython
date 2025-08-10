import network
from time import sleep

wifi = network.WLAN(network.STA_IF)
wifi.active(True)  # 观察是否还会触发复位
print("Wi-Fi 模块已激活")
# wifi.connect("SSID", "PASSWORD")  # 可后续再试