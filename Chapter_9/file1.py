import os
print(os.getcwd())


myfile = open("text.txt")
data = myfile.read()

print(data) 

myfile.close()  # Close the file    