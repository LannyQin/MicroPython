from dino.img import cactus1,cactus2
from common.oled_show_character import show_character
from random import randint

data=[]


class YouDie(Exception):
    pass


class Cactus:
    def __init__(self,oled,dino):
        self.oled=oled
        self.type=randint(0,1)
        self.img=cactus1 if self.type==0 else cactus2
        self.x=127
        self.y=40
        self.width=11 if self.type==0 else 9
        self.alive=True
        self.dino=dino
    
    def show(self):
        if self.x+self.width<-5:
            self.alive=False
            return
        show_character(self.oled,self.img,self.x,self.y,18,16)
        self.update()
        self.check()
    
    def update(self):
        self.x-=5
    
    def check(self):
        if (self.dino.y+18>self.y) and ((self.x < self.dino.x <self.x+self.width) or (self.x < self.dino.x+16 < self.x+self.width)):
            raise YouDie()


class CactusManager:
    def __init__(self,oled,dino):
        self.oled=oled
        self.cactus=[]
        self.last_update=15
        self.dino=dino
    
    def update(self):
        if self.last_update<=0:
            if randint(1,5)==1:
                self.cactus.append(Cactus(self.oled,self.dino))
                self.last_update=15
        self.last_update-=1
        kill_list=[]
        for i in range(len(self.cactus)):
            if not self.cactus[i].alive:
                kill_list.append(i)
            else:
                self.cactus[i].show()
        for i in kill_list:
            del self.cactus[i]