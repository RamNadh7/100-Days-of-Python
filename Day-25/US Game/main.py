import turtle
import pandas

screen=turtle.Screen()
screen.title("US States Game")
IMAGE="blank_states_img.gif"
Guessed_states=[]

screen.addshape(IMAGE)

turtle.shape(IMAGE)
data=pandas.read_csv("50_states.csv")

states_list=data.state.to_list()

while len(Guessed_states) < 50:
    usr_answer=screen.textinput(title=f"{len(Guessed_states)}/50 States Correct",prompt="What's the another state name?").title()
    if usr_answer=="Exit":
        missingstates=[]
        for state in states_list:
            if state not in Guessed_states:
                missingstates.append(state) 
        new_data=pandas.DataFrame(missingstates)
        new_data.to_csv("Missed States.csv")
        break
        
    if usr_answer in states_list:
        Guessed_states.append(usr_answer)
        tim=turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        state=data[data.state==usr_answer]
        tim.goto(int(state.x),int(state.y))
        tim.write(usr_answer)



