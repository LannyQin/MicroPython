import network
from machine import Timer
from time import time


class WifiManager:
    '''自定义WiFi管理模块，可以设置超时时长'''
    
    def __init__(self,ssid,password,timeout=10,timeout_raise_error=False):
        self.ssid=ssid
        self.password=password
        self.timeout=timeout
        self.timeout_raise_error=timeout_raise_error
        self.WLAN=network.WLAN(network.STA_IF)
    
    def connect(self):
        self.t0=time()  #秒级
        self.WLAN.connect(self.ssid,self.password)
        self.check_is_connected_timer=Timer(3)
        self.check_is_connected_timer.init(mode=Timer.PERIODIC,period=100,callback=self.checker)
    
    def checker(self,timer_obj):
        if self.WLAN.isconnected:
            timer_obj.deinit()
        time_now=time()
        if time_now > self.t0+self.timeout:
            self.timer_obj.deinit()
            self.active(False)
            if self.timeout_raise_error:                
                raise TimeoutError
            
    def active(self,value=None):
        if value is None:
            return self.WLAN.active()
        else:
            self.WLAN.active(value)
    
    def isconnected(self):
        return self.WLAN.isconnected()
    
    def config(self,*args,**kwargs):
        return self.WLAN.config(*args,**kwargs)
    
    def ifconfig(self):
        return self.WLAN.ifconfig()
    
    def scan(self):
        return self.WLAN.scan()
    
    def disconnect(self):
        return self.WLAN.disconnect()