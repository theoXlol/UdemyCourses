def greet():
    print("Hello")
    print("How are you")
    print("Good")



#Functions that allows for inputs


def greet_with_name(name):
    print(f"hello {name}")
    print(f"How do you do {name}?")





def life_in_weeks(age):
    maths = 90 - age
    weeks = maths * 52
    print(f"You have {weeks} weeks left.")



def caeser_cypher():
    user_input = input("Type a message: \n").lower()
    shift = int(input("Type a shift number: \n"))
    cipher_text = ""
    for letter in user_input:
        position = ord(letter)
        new_position = position + shift
        new_letter = chr(new_position)
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
    
caeser_cypher()