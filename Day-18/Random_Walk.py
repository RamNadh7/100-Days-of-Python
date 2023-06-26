from turtle import Turtle,Screen
import random


the_turtle=Turtle()
screen=Screen()
screen.colormode(255)
the_turtle.pensize(10)
the_turtle.speed("fastest")

direction=[0,90,180,270]


def shape():
    the_turtle.pencolor(red,green,blue)
    # for i in range():
    the_turtle.forward(30)
    the_turtle.setheading(random.choice(direction))



for sides in range(300):
    red=random.randint(1,255)
    green=random.randint(1,255)
    blue=random.randint(1,255)
    shape()






screen.exitonclick()