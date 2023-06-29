from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.score=0
        self.goto(0,260)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"score: {self.score}", align="center", font=("ariel",24,"normal"))
        

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=("ariel",24,"normal"))