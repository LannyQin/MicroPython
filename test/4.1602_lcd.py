from machine import Pin,SoftI2C

from libs.i2c_lcd import I2cLcd

i2c=SoftI2C(scl=Pin(25),sda=Pin(26),freq=100000)

#获取I2C设备地址
address=i2c.scan()[0]

#定义I2cLcd对象
i2clcd=I2cLcd(i2c,address,2,16)

#打印Hello，world
i2clcd.backlight_on()
i2clcd.putstr('Hello,world!')