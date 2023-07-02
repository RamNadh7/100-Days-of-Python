from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen=Screen()
screen.setup(height=600,width=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")


snake=Snake()
food=Food()
Scoreboard=Scoreboard()

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

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend() 
        Scoreboard.increase_score()

    
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        Scoreboard.reset()
        snake.reset()


    
    for seg in snake.segments[1:]:
        if  snake.head.distance(seg) < 10:
            Scoreboard.reset()
            snake.reset()




screen.exitonclick()