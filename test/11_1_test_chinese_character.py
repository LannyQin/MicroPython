from machine import Pin,SoftI2C
from libs.ssd1306_1 import SSD1306_I2C

i2c=SoftI2C(sda=Pin(21),scl=Pin(22))
address=i2c.scan()[0]
oled=SSD1306_I2C(128,64,i2c,address)

oled.font_load("font/GB2312-16.fon")

oled.fill(0)
oled.text('你好',0,0)
oled.show()