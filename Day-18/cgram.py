"""
This code is used to generate the different colors from the picture
import colorgram

colors=colorgram.extract('pic.jpg',30)
rgb=[]
for col in colors:
    red=col.rgb.r
    green=col.rgb.g
    blue=col.rgb.b
    temp=(red,green,blue)
    rgb.append(temp)

print(rgb)


[(215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]

"""




from turtle import Turtle,Screen
import  random


color_list=[(215, 166, 17), (230, 239, 234), (205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58), (8, 109, 166), (42, 13, 24), (160, 29, 25), (12, 23, 52), (34, 122, 62), (59, 23, 18), (9, 32, 26), (186, 156, 173), (63, 166, 88), (171, 57, 42), (156, 208, 215), (94, 183, 167), (205, 99, 95), (240, 200, 3), (213, 174, 198), (28, 37, 105), (187, 99, 110), (163, 209, 197), (220, 177, 173), (14, 105, 56)]

turtle=Turtle()
screen=Screen()
turtle.speed(10)
screen.colormode(255)
turtle.penup()

turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    col= random.choice(color_list)
    turtle.dot(20,col)
    turtle.forward(50)

    if dot_count % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)

    




screen.exitonclick()