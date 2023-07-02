from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.score=0
        with open("data.txt") as file:
            self.highscore=int(file.read()) 
        self.goto(0,260)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score: {self.score} High Score= {self.highscore}", align="center", font=("ariel",24,"normal"))
        

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over", align="center", font=("ariel",24,"normal"))