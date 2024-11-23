print("Welcome to the tip calculator!")

price = float(input("What was the total bill? $ "))

tip = int(input("How much tip would you like to give? 10, 12, or 15 ?"))

people = int(input("How many people to split the bill? "))

new_number = int(price)

pay = round(((new_number+(new_number*(tip/100)))/people),3)

print("Each person should pay:",pay)