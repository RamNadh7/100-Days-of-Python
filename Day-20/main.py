"""
Check Day 21 for full code
"""

from turtle import Turtle,Screen
import time
from snake import Snake

screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")


snake=Snake()
# food=Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()