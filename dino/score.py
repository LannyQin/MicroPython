class Score:
    def __init__(self,oled):
        self.oled=oled
        self.score=0
        self.high_score=self.read_high_score()
    
    def read_high_score(self):
        with open('dino/history_high_score.txt','r')as file:
            return file.read()
    
    def write_high_score(self):
        self.score-=1
        if self.score>int(self.high_score):
            with open('dino/history_high_score.txt','w+') as file:
                file.write(str(self.score))
    
    def update(self):
        score_str=str(self.score)
        score_text='0'*(5-len(score_str))+score_str
        self.oled.text(score_text,88,0)
        self.score+=1
        
        high_score_text='0'*(5-len(self.high_score))+self.high_score
        self.oled.text(high_score_text,40,0)