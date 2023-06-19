#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

def right_turn():
    turn_left()
    turn_left()
    turn_left()

def jump():   
        turn_left()
        move()
        right_turn()
        move()
        right_turn()
        move()
        if not at_goal():
            turn_left()

while not at_goal():
    if front_is_clear():
            move()
    else:
        jump()