age = int(input("Enter your age:"))

if (age < 18):
    print("You are a minor.") # indentation behind print statement is important it means that you are INSIDE the if statement

elif (age >= 18 and age < 25):
    print("You are an adult.")

else:
    print("You are a senior citizen.")