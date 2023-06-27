from turtle import Turtle,Screen

the_turtle=Turtle()
screen=Screen()


def move_fwd():
    the_turtle.forward(10)

def move_back():
    the_turtle.backward(10)

def move_left():
    the_turtle.left(10)

def move_right():
    the_turtle.right(10)

def clear():
    the_turtle.clear()
    the_turtle.reset()

screen.listen()
screen.onkey(move_fwd, "w")
screen.onkey(move_back, "s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear,"c")















screen.exitonclick()