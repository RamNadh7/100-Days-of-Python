from turtle import Turtle,Screen


the_turtle=Turtle()

for t in range(15):
    the_turtle.forward(7)
    the_turtle.penup()
    the_turtle.forward(7)
    the_turtle.pendown()

screen=Screen()
screen.exitonclick()