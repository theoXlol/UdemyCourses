import random

def spiel():

    optionen = ["Stein", "Papier", "Schere"]


    benutzerwahl = input("Wähle (Stein, Papier, Schere): ").capitalize()


    if benutzerwahl not in optionen:
        print("Ungültige Wahl! Bitte gib 'Stein', 'Papier' oder 'Schere' ein.")
        return


    computerwahl = random.choice(optionen)
    print(f"Der Computer wählt: {computerwahl}")


    if benutzerwahl == computerwahl:
        print("Unentschieden!")
    elif (benutzerwahl == "Stein" and computerwahl == "Schere") or \
         (benutzerwahl == "Papier" and computerwahl == "Stein") or \
         (benutzerwahl == "Schere" and computerwahl == "Papier"):
        print("Du hast gewonnen!")
    else:
        print("Der Computer hat gewonnen!")
spiel()