def greet():
    print("Hello")
    print("How are you")
    print("Good")

greet()

#Functions that allows for inputs


def greet_with_name(name):
    print(f"hello {name}")
    print(f"How do you do {name}?")

greet_with_name("sigma")



def life_in_weeks(age):
    maths = 90 - age
    weeks = maths * 52
    print(f"You have {weeks} weeks left.")
life_in_weeks(20)