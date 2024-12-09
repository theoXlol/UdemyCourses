print("Welcome to python Pizza Deliveries! ")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni Y or N: ")
extra_cheese = input("Do you want extra cheese Y or N:")
bill = 0

if size == "s":
    bill = 15
elif size == "m":
    bill = 20
else:
    bill = 25

if pepperoni == "y":
    bill += 2
if extra_cheese == "y":
    bill +=3

print(f"Your total order is ${bill} ")