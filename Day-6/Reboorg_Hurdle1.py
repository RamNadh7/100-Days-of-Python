# use this link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

def right_turn():
    turn_left()
    turn_left()
    turn_left()

def jump():
    for i in range (6):    
        move()
        turn_left()
        move()
        right_turn()
        move()
        right_turn()
        move()
        turn_left()

jump()