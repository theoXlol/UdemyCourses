import random


#random_number_0_to_1 = random.random() * 10
#print(random_number_0_to_1)

#random_float = random.uniform (1,10)
#print(random_float)

head_or_tails = random.randint(1,2)

if head_or_tails == 1:
    print("Head")
else:
    print("Tails")