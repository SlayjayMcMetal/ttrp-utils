import random 
def roll_dice(sides,num_dice):
    total=0
    for i in range(num_dice):
        result=random.randint(1,sides)
        total+=result
    return total


def cast_fireball(wisdom):
    print("Casting fireball")
    damage=roll_dice(6,10)+wisdom
    print(f"The fire did {damage} damage")




#print("welcome to duh dice boi")
#sides = int(input("How many die sides?"))
#num_dice = int(input("How many num_dice?"))
#result=roll_dice(sides,num_dice)
#print(f"Roll result is {result}")

wisdom = int(input("What is yer wisdom?"))
user_choice = input("Would you like to cast fireball? [y/n]")
if user_choice == "y":
    cast_fireball(wisdom)
else:
    print("Aight then")
