# snake, water and gun game

# 1 for snake
# -1 for water
# 0 for gun


import random

# computer = -1

random_number = random.choice([1, -1, 0])

youstr = input("Enter your choice: ")
youDict = {"snake": 1, "water": -1, "gun": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[random_number]}")




if(random_number == -1 and you == 1):
    print("You win")
elif(random_number == -1 and you == 0):
    print("You win")
elif(random_number == 0 and you == -1):
    print("You win")
elif(random_number == you):
    print("Draw")
else:
    print("something went wrong")

# testing commit