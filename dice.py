import random

l = range(1,7)
dice = random.choice(l)
ask = input("Would you like to roll the dice (y/n)?: ").strip().lower()

if ask == "y":
    print("Dice has rolled a {}!".format(dice))
else:
    print("Okay, maybe another time?")
    
while True:
    dice = random.choice(l)
    again = input("Would you like to roll again (y/n)?: ").strip().lower()
    if again == "y":
        print("Dice has rolled a {}!".format(dice))
    else:
        print("Another time then!")
        break

