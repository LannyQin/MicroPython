from machine import Pin,SoftI2C
from time import sleep_ms

from libs.ssd1306 import SSD1306_I2C
from dino.dino_class import Dino
from dino.ground_class import Ground
from dino.cactus_class import CactusManager,YouDie
from dino.score import Score
from dino.fps import FPS
from common.oled_show_character import show_character
from dino.img import start,restart

i2c=SoftI2C(scl=Pin(22),sda=Pin(21))
print('scanning')
address=i2c.scan()[0]
print('scanned')

oled=SSD1306_I2C(128,64,i2c,address)

button=Pin(14,Pin.IN,Pin.PULL_DOWN)

dino=Dino(oled)
ground=Ground(oled,dino)
cactus_manager=CactusManager(oled,dino)
score=Score(oled)
fps=FPS(oled)


def main():
    try:
        while True:
            oled.fill(0)
            cactus_manager.update()
            dino.show()
            if button.value()==1 and dino.status==0:
                dino.status=1
            dino.update()
            ground.show()
            score.update()
            fps.update()
            oled.show()
    except YouDie:
        dino.show()
        ground.show()
        score.update()
        fps.update()
        show_character(oled,restart,56,14,14,16)
        oled.text('Restart',36,29)
        oled.show()
        score.write_high_score()
        sleep_ms(1500)
        
        while True:
            if button.value()==1:
                break
            sleep_ms(15)
        dino.__init__(oled)
        ground.__init__(oled,dino)
        cactus_manager.__init__(oled,dino)
        score.__init__(oled)
        fps.__init__(oled)
        main()

oled.fill(0)
dino.show()
ground.show()
score.update()
show_character(oled,start,56,14,13,16)
oled.text('Start',44,29)
oled.show()

while True:
    if button.value()==1:
        break
    sleep_ms(15)
    
main()