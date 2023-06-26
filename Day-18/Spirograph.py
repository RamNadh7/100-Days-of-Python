from turtle import Turtle, Screen
import random

the_turtle=Turtle()
screen=Screen()
the_turtle.speed(10)
screen.colormode(255)


def random_color():
    red=random.randint(1,255)
    green=random.randint(1,255)
    blue=random.randint(1,255)
    color=(red,green,blue)
    return color    


def draw(size):
    for i in range(int(360/size)):
        the_turtle.color(random_color())
        the_turtle.circle(150)
        the_turtle.setheading(the_turtle.heading()+size)



draw(10)



screen.exitonclick()
