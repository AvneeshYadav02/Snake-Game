from turtle import Turtle

ALLIGNMENT = 'center'
FONT = ("Times New Roman", 15, "normal")
GAME_OVER_FONT = ("Times New Roman", 30, "bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt', "r") as hs:
            self.high_score = hs.read()
            self.high_score = int(self.high_score)
            hs.close()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x=0, y=280)
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(arg=f"Your Score: {self.score} | High Score: {self.high_score}", align=ALLIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', "w") as hs:
                hs.write(str(self.high_score))
                hs.close()
        self.score = 0      
        self.update_score()   
        
    def score_up(self):
        self.score += 1
        self.clear()
        self.update_score()