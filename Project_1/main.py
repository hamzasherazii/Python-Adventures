# snake, water and gun game

# 1 for snake
# -1 for water
# 0 for gun

computer = -1
youstr = input("Enter your choice: ")
youDict = {"snake": 1, "water": -1, "gun": 0}

you = youDict[youstr]

if(computer == -1 and you == 1):
    print("You win")
elif(computer == 1 and you == 0):
    print("You win")
elif(computer == 0 and you == -1):
    print("You win")
elif(computer == you):
    print("Draw")
else:
    print("something went wrong")

# testing commit