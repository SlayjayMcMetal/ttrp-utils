import random 
print("welcome to duh dice boi")
sides = int(input("How many die sides?"))
num_dice = int(input("How many num_dice?"))
for i in range(num_dice):
    print(f"rolling a d{sides}...")
    result=random.randint(1,sides)
    print(f"{result}")

