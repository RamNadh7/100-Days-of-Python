# from turtle import Turtle,Screen

# Timmy=Turtle()
# print(Timmy)
# Timmy.shape("turtle")
# Timmy.color("coral")
# Timmy.forward(100)

# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table=PrettyTable()

table.field_names=["Pokemon","Type"]
table.add_rows(
    [
    ["Pikachu","electric"],
    ["Squirtle","Water"],
    ["Charmandar","Fire"]
    ]
)
table.align="l"
print(table)