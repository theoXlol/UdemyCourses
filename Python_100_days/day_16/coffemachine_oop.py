# ...existing code...

class CoffeeMachine:
		self.resources = {
			"water": 300,
			"milk": 200,
			"coffee": 100
		}
		self.menu = {
			"espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
			"latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
			"cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
		}
		self.money = 0.0

	def print_report(self):
		print(f"Water: {self.resources['water']}ml")
		print(f"Milk: {self.resources['milk']}ml")
		print(f"Coffee: {self.resources['coffee']}g")
		print(f"Money: ${self.money}")

	def is_resource_sufficient(self, drink):
		for item in ["water", "milk", "coffee"]:
			if self.resources[item] < self.menu[drink][item]:
				print(f"Sorry there is not enough {item}.")
				return False
		return True

	def process_coins(self):
		print("Please insert coins.")
		total = int(input("How many quarters?: ")) * 0.25
		total += int(input("How many dimes?: ")) * 0.10
		total += int(input("How many nickels?: ")) * 0.05
		total += int(input("How many pennies?: ")) * 0.01
		return total

	def make_coffee(self, drink):
		for item in ["water", "milk", "coffee"]:
			self.resources[item] -= self.menu[drink][item]
		print(f"Here is your {drink} ☕️. Enjoy!")

	def run(self):
		is_on = True
		while is_on:
			choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
			if choice == "off":
				is_on = False
			elif choice == "report":
				self.print_report()
			elif choice in self.menu:
				if self.is_resource_sufficient(choice):
					payment = self.process_coins()
					cost = self.menu[choice]["cost"]
					if payment >= cost:
						change = round(payment - cost, 2)
						if change > 0:
							print(f"Here is ${change} in change.")
						self.money += cost
						self.make_coffee(choice)
					else:
						print("Sorry that's not enough money. Money refunded.")
			else:
				print("Invalid selection.")


if __name__ == "__main__":

	class CoffeeMachine:
		def __init__(self):
			self.resources = {
				"water": 300,
				"milk": 200,
				"coffee": 100
			}
			self.menu = {
				"espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
				"latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
				"cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
			}
			self.money = 0.0

		def print_report(self):
			print(f"Water: {self.resources['water']}ml")
			print(f"Milk: {self.resources['milk']}ml")
			print(f"Coffee: {self.resources['coffee']}g")
			print(f"Money: ${self.money}")

		def is_resource_sufficient(self, drink):
			for item in ["water", "milk", "coffee"]:
				if self.resources[item] < self.menu[drink][item]:
					print(f"Sorry there is not enough {item}.")
					return False
			return True

		def process_coins(self):
			print("Please insert coins.")
			total = int(input("How many quarters?: ")) * 0.25
			total += int(input("How many dimes?: ")) * 0.10
			total += int(input("How many nickels?: ")) * 0.05
			total += int(input("How many pennies?: ")) * 0.01
			return total

		def make_coffee(self, drink):
			for item in ["water", "milk", "coffee"]:
				self.resources[item] -= self.menu[drink][item]
			print(f"Here is your {drink} ☕️. Enjoy!")

		def run(self):
			is_on = True
			while is_on:
				choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
				if choice == "off":
					is_on = False
				elif choice == "report":
					self.print_report()
				elif choice in self.menu:
					if self.is_resource_sufficient(choice):
						payment = self.process_coins()
						cost = self.menu[choice]["cost"]
						if payment >= cost:
							change = round(payment - cost, 2)
							if change > 0:
								print(f"Here is ${change} in change.")
							self.money += cost
							self.make_coffee(choice)
						else:
							print("Sorry that's not enough money. Money refunded.")
				else:
					print("Invalid selection.")


	if __name__ == "__main__":
		machine = CoffeeMachine()
		machine.run()
