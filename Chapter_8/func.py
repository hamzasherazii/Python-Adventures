

# This is called function definition
def add():
    print("Addition of two numbers")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: ")) 
    print("Sum of two numbers is: ", a+b)

def sub():
    print("Subtraction of two numbers")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: ")) 
    print("Subtraction of two numbers is: ", a-b)

def mul():
    print("Multiplication of two numbers")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: ")) 
    print("Multiplication of two numbers is: ", a*b)

def div():
    print("Division of two numbers")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: ")) 
    print("Division of two numbers is: ", a/b)


# This is called function calling
add()
sub()
mul()
div()