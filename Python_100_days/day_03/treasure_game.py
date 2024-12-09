from tkinter.messagebox import YESNO

print("Welcome to Treasure island. Your mission is to find the treasure")
play_game = input("Do you want to play the game? Y or N:")

if play_game == "y" :
    door1 = input("You find 2 doors wich one will you take? Left or Right: ")
if door1 == "left":
    print("Game Over")
else:
    boat = input("You find an Lake do you want to wait for a boat? Y or N")
  if boat == "y":
    door_2 = input("You find 3 doors wich one are you going to open? 1,2 or 3:")
  else:
      print("Game Over")
       if door_2 == 1:
         print("game Over")
       elif door_2 == 2:
           print("You won!")
       else:
            print("Game Over")
