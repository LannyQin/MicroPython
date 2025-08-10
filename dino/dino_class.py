from dino.img import dino1,dino2
from common.oled_show_character import show_character

class Dino:
    def __init__(self,oled):
        self.oled=oled
        self.img=[dino1,dino2]
        self.img_now=False #False=0,True=1
        self.x=10
        self.y=40
        self.status=0
        self.waiting=1
    
    def show(self):
        img=self.img[1] if self.img_now else self.img[0]
        show_character(self.oled,img,self.x,self.y,18,16)
        #self.oled.show()
    
    def update(self):
        self.img_now=not self.img_now
        if self.status==1:
            if self.y>-20:
                self.y-=10
            else:
                if self.waiting>0:
                    self.waiting-=1
                else:
                    self.status=2
                    self.waiting=1
        if self.status==2:
            if self.y<40:
                self.y+=10
            else:
                self.status=0
                self.y=40
                