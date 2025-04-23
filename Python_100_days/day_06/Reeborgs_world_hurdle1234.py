#You can use the code on https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json
#The Code works on Hurdle 1, Hurdle 2, Hurdle 3 and Hurdle 4 have fun!(You can only use it on this Website otherwise you will get a Syntax
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()

    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()