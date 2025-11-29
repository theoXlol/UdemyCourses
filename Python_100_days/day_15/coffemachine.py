def main():
    # Initialize resources
    Water = 300
    Milk = 200
    Coffee = 100
    Money = 0.0
    
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ")
        if user_input == "off":
            print("Turning off the coffee machine. Goodbye!")
            break
        elif user_input == "report":
            print(f"Water: {Water}ml")  
            print(f"Milk: {Milk}ml")
            print(f"Coffee: {Coffee}g")
            print(f"Money: ${Money:.2f}") 
        elif user_input == "espresso":
            if Water >= 50 and Coffee >= 18:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                total_inserted = quarters * 0.25 + dimes * 0.10
                total_inserted += nickels * 0.05 + pennies * 0.01
                if total_inserted >= 1.50:
                    change = round(total_inserted - 1.50, 2)
                    if change > 0:
                        print(f"Here is ${change:.2f} in change.")
                    print("Here is your espresso. Enjoy!")
                    Water -= 50
                    Coffee -= 18
                    Money += 1.50
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                if Water < 50:
                    print("Sorry there is not enough water.")
                elif Coffee < 18:
                    print("Sorry there is not enough coffee.")
        elif user_input == "latte":
            if Water >= 200 and Milk >= 150 and Coffee >= 24:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                total_inserted = quarters * 0.25 + dimes * 0.10
                total_inserted += nickels * 0.05 + pennies * 0.01
                if total_inserted >= 2.50:
                    change = round(total_inserted - 2.50, 2)
                    if change > 0:
                        print(f"Here is ${change:.2f} in change.")
                    print("Here is your latte. Enjoy!")
                    Water -= 200
                    Milk -= 150
                    Coffee -= 24
                    Money += 2.50
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                if Water < 200:
                    print("Sorry there is not enough water.")
                elif Milk < 150:
                    print("Sorry there is not enough milk.")
                elif Coffee < 24:
                    print("Sorry there is not enough coffee.")
        elif user_input == "cappuccino":
            if Water >= 250 and Milk >= 100 and Coffee >= 24:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                total_inserted = quarters * 0.25 + dimes * 0.10
                total_inserted += nickels * 0.05 + pennies * 0.01
                if total_inserted >= 3.00:
                    change = round(total_inserted - 3.00, 2)
                    if change > 0:
                        print(f"Here is ${change:.2f} in change.")
                    print("Here is your cappuccino. Enjoy!")
                    Water -= 250
                    Milk -= 100
                    Coffee -= 24
                    Money += 3.00
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                if Water < 250:
                    print("Sorry there is not enough water.")
                elif Milk < 100:
                    print("Sorry there is not enough milk.")
                elif Coffee < 24:
                    print("Sorry there is not enough coffee.")
        else:
            print("Invalid input. Please enter espresso, latte, cappuccino, report, or off.")

            
main()