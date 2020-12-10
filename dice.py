import random

def roll_dice():
    dice = random.choice(chance)
    return dice

chance = range(1,7)
roll_dice()
ask = input("Would you like to roll the dice (y/n)?: ").strip().lower()

if ask == "y":
    print("Dice has rolled a {}!".format(roll_dice()))
else:
    print("Okay, maybe another time?")
    
while True:
    roll_dice()
    again = input("Would you like to roll again (y/n)?: ").strip().lower()
    if again == "y":
            print("Dice has rolled a {}!".format(roll_dice()))
    else:
        print("Another time then!")
        break

