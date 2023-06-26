from turtle import Turtle,Screen
import random


the_turtle=Turtle()
screen=Screen()
screen.colormode(255)


def shape(num,red,green,blue):
    degrees=360/num
    the_turtle.pencolor(red,green,blue)
    for i in range(num):
        the_turtle.forward(100)
        the_turtle.right(degrees)



for sides in range(3,11):
    red=random.randint(1,255)
    green=random.randint(1,255)
    blue=random.randint(1,255)
    shape(sides,red,green,blue)






screen.exitonclick()