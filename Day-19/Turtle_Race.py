from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
usr_bet=screen.textinput(title="Make your Bet",prompt="Which color turtle will win?")
colors=["red","green","blue","purple","yellow","orange"]
y_positions=[-70,-40,0,30,60,90]
all_turtles=[]

for t in range(0,6):
    the_turtle=Turtle(shape="turtle")
    the_turtle.color(colors[t])
    the_turtle.penup()
    the_turtle.goto(x=-230, y=y_positions[t])
    all_turtles.append(the_turtle)

if usr_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==usr_bet:
                print(f"You've won! the {winning_color} turtle is winner")
            else:
                print(f"You've lost! the {winning_color} turtle is winner")

        distance=random.randint(0,10)
        turtle.forward(distance)




screen.exitonclick()