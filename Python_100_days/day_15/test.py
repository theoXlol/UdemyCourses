

def user_input():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        if choice in ["espresso", "latte", "cappuccino"]:
            print("Thank you for your order")
            return choice
        else:
            print("Wrong Input")

def turn_coffemachine_off():
    worker_input = input("Would you like to turn the machine off? (type 'off'): ").strip().lower()
    if worker_input == "off":
        # signal to caller to stop the main loop / program
        return True
    return False

def ressoure_report():
    water = 100
    milk = 50
    coffee = 76
    money = 5.99
    all_ressources = {"water": water, "milk": milk, "coffee": coffee, "money": money}
    user_input_str = input("Would you like to get a report of the available resources? (report): ").strip().lower()
    if user_input_str == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
    return all_ressources

def ressource_check(choice, all_ressources):
    water = all_ressources["water"]
    milk = all_ressources["milk"]
    coffee = all_ressources["coffee"]

    if choice == "espresso":
        # Beispielbedarf: 50 water, 18 coffee
        if water >= 50 and coffee >= 18:
            print(f"You ordered a {choice}")
        else:
            print("Not enough resources for espresso")
    elif choice == "latte":
        # Beispielbedarf: 200 water, 150 milk, 24 coffee
        if water >= 200 and milk >= 150 and coffee >= 24:
            print(f"You ordered a {choice}")
        else:
            print("Not enough resources for latte")
    elif choice == "cappuccino":
        # Beispielbedarf: 250 water, 100 milk, 24 coffee
        if water >= 250 and milk >= 100 and coffee >= 24:
            print(f"You ordered a {choice}")
        else:
            print("Not enough resources for cappuccino")
            
def coin_machine():
    # Quarters = 0.25
    # Dimes = 0.10
    # Nickles = 0.05
    # Pennies = 0.01
    quarters = int(input("How much Quarters?:"))
    dimes = int(input("How many Dimes?:"))
    nickles = int(input("How many Nickles?:"))
    pennies = int(input("how many pennies?:"))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total
    
def check_transaction(total, choice):
    drink_prices = {"espresso": 1.5, "latte": 2.5, "cappuccino": 3.0}
    if total >= drink_prices[choice]:
        change = round(total - drink_prices[choice], 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {choice}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

def main():
    """
    Simple interactive loop that demonstrates calling the existing functions.
    Run the script and follow prompts. To stop, type 'off' when asked to turn the machine off.
    """
    # Initialize resources from the existing function (which may optionally print a report)
    all_ressources = ressoure_report()

    while True:
        # Allow operator to turn machine off
        if turn_coffemachine_off():
            print("Turning the coffee machine off. Bye.")
            break

        # Get user choice (will only return a valid drink)
        choice = user_input()

        # Check resources for selected drink
        ressource_check(choice, all_ressources)

        # Process coins and transaction
        total = coin_machine()
        check_transaction(total, choice)

if __name__ == "__main__":
    main()
    