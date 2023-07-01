import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
CarManager=CarManager()
Scoreboard=Scoreboard()
screen.listen()

screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    CarManager.create_car()
    CarManager.move_car()

    for car in CarManager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            Scoreboard.game_over( )

            
    if player.is_finishline():
        player.goto_start()
        CarManager.level_up()
        Scoreboard.increase_level()

screen.exitonclick()