# File handling
# We can do 4 main things in file handling
# 1. Create a file
# 2. Write to a file
# 3. Read from a file
# 4. Close file

# Type of files
# 1. Text files (.txt , .py , .csv , .json)
# 2. Binary files (.jpg , .png , .pdf , .exe) 


# Syntax
# file_object = open("file_name" , "mode")
# modes
# r - read
# w - write
# a - append
# x - create

# Creating a file
# f = open("new_file.txt" , "x")

# Writing to a file
# f = open("new_file.txt" , "w")
# f.write("Hello World from programing communities\n")
# f.close()

# Read from a file
# f = open("new_file.txt " , "r" )
# print(f.read())
# f.close()

# Append to a file
# f = open("new_file.txt" , "a")
# f.write("Hello World\n")
# f.close()

# Using with statement to close a file
# with open("new_file.txt" , "a") as file:
#     file.write("Hello World on line no.3\n")


# file = open("new_file.txt " , "a")
# file.write("This is from outside statement \n")
# file.close()

f = open("class_11.py" , "a")
f.write("try \n num1 = int(input('Enter a number: ')) \n except  \n print('Invalid input') \n")
f.close()