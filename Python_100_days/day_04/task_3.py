import random

friends = ["Roman", "Theodor", "Christopher", "Veronika"]

card = random.randint(1, 4)

if card == 1:
    print (friends[0])
elif card == 2:
    print (friends[1])
elif card == 3:
    print (friends[2])
else:
    print (friends[3])