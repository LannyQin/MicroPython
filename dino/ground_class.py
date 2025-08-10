from random import randint

class Ground:
    def __init__(self,oled,dino):
        self.oled=oled
        self.y=55
        self.grass=[]
        self.seed=1
        self.dino=dino
        
    def show(self):
        for i in range(128):
            self.oled.pixel(i,self.y,1)
        if self.dino.status==0:
            for i in range(12,14):
                self.oled.pixel(i,self.y,0)
            for i in range(20,22):
                self.oled.pixel(i,self.y,0)
            if self.dino.img_now:
                for i in range(16,18):
                    self.oled.pixel(i,self.y,0)
            else:
                for i in range(15,17):
                    self.oled.pixel(i,self.y,0)
        
        if randint(1,8) == self.seed:
            self.grass.append(Grass(self.oled))
        self.seed+=1
        if self.seed>8:
            self.seed=1
        kill_list=[]
        for i in range(len(self.grass)):
            if not self.grass[i].alive:
                kill_list.append(i)
            else:
                self.grass[i].show()
        for i in kill_list:
            del self.grass[i]
                
        #self.oled.show()

class Grass:
    def __init__(self,oled):
        self.oled=oled
        self.x=127
        self.y=57
        self.length=randint(4,7)
        self.alive=True
    
    def show(self,update=True):
        if self.x+self.length<0:
            self.alive=False
            return
        for i in range(self.x,self.x+self.length):
            self.oled.pixel(i,self.y,1)
        if update:
            self.update()
    
    def update(self):
        self.x-=5