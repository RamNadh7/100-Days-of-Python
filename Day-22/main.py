from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

Screen=Screen()
Screen.bgcolor("black")
Screen.setup(width=800,height=600)
Screen.title("Ping Pong")
Screen.tracer(0)


r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()



Screen.listen()
Screen.onkey(r_paddle.go_up,"Up")
Screen.onkey(r_paddle.go_down,"Down")
Screen.onkey(l_paddle.go_up,"w")
Screen.onkey(l_paddle.go_down,"s")


game_on=True
while game_on:
    time.sleep(ball.move_speed)
    Screen.update()
    ball.move()
 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    
    if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.lpoint()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rpoint() 

Screen.exitonclick( )