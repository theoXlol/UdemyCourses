print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <=12:
        bill = 5
        print("You need to pay $5.")
    elif age <=12:
        bill = 7
        print("You need to pay $7 ")
    elif age  >=45 and age <= 55:
        print(" you can go for free ")
    else:
        bill = 12
        print("You need to pay $12.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes n for No")
    if wants_photo == "y":
        #Add $3 to the bill
       bill += 3

    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have ot grow taller before you can ride")