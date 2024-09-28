import os

# Specify the directory path
directory = '/coding'

# Get the list of files and directories in the specified directory
contents = os.listdir(directory)

# Print the contents
for item in contents:
    print(item)