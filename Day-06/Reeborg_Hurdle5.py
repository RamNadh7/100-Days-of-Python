#Use this link for challenge : https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def right_turn():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while at_goal()==False:
    if right_is_clear():
        right_turn()
        move()
    elif front_is_clear():
        move()
    else: turn_left()