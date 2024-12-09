import random
import string

def generate_password(letters_count, digits_count, symbols_count):

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation


    password_letters = random.choices(letters, k=letters_count)
    password_digits = random.choices(digits, k=digits_count)
    password_symbols = random.choices(symbols, k=symbols_count)


    password = password_letters + password_digits + password_symbols


    random.shuffle(password)


    return ''.join(password)


letters_count = int(input("Wie viele Buchstaben möchtest du im Passwort? "))
digits_count = int(input("Wie viele Zahlen möchtest du im Passwort? "))
symbols_count = int(input("Wie viele Sonderzeichen möchtest du im Passwort? "))


password = generate_password(letters_count, digits_count, symbols_count)
print(f"Dein generiertes Passwort ist: {password}")