# Test it out in:https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
# If it is over 1000 steps its stuck and you need to restart have fun!(Only works on this website otherwise syntax)
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
     if right_is_clear():
         turn_right()
         move()
     elif front_is_clear():
         move()
     else:
         turn_left()