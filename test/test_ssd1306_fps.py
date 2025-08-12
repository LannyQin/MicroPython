from machine import Pin,SoftI2C,RTC
from libs.ssd1306 import SSD1306_I2C

i2c=SoftI2C(scl=Pin(22),sda=Pin(21))
print('scanning')
address=i2c.scan()[0]
print('scanned')

oled=SSD1306_I2C(128,64,i2c,address)

rtc=RTC()
frames=[]
t=rtc.datetime()
frames.append([t[6],t[7]])

def frame():
    t=rtc.datetime()
    oled.fill(0)
    kill=0
    for i in range(len(frames)):
        if frames[i][1]<=t[7] and (t[6]>=frames[i][0]+1 or (frames[i][0]==59 and t[6]==0)):
            kill+=1
    if kill>0:
        del frames[:kill]
    oled.text('FPS:'+str(len(frames)),0,0)
    oled.show()
    frames.append([t[6],t[7]])

while True:
    frame()
            