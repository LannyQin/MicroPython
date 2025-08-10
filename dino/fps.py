from machine import Timer

class FPS:
    def __init__(self,oled):
        self.oled=oled
        self.timer=Timer(0)
        self.timer.init(mode=Timer.PERIODIC,period=1000,callback=self.check)
        self.times=0
        self.times_show=0
    
    def check(self,timer_obj):
        self.times_show=self.times
        self.times=0
    
    def update(self):
        self.times+=1
        self.oled.text(f'FPS {("0" if len(str(self.times_show))==1 else "")+str(self.times_show)}',80,8)