# New Type
# List - Mutable Type 
# In context of other languages: Array

fruits = ["apple", "banana", "cherry"]

# Exalmple of Students

student1 = "Hassan"
student2 = "Ali"
student3 = "Ahmed"
student4 = "Omar"
student5 = "Sami"
student6 = "Zaid"

# print(f"Student 1: {student1}")
# Index       0      , 1    ,   2  ,   3   ,   4   ,   5
students = ["Hassan", "Ali", "Ahmed", "Omar", "Sami", "Zaid"]
print(students, "Original List")




# Adding new student to the list
students.append("haider")
# List After Append ['Hassan', 'Ali', 'Ahmed', 'Omar', 'Sami', 'Zaid', 'haider']
print(students , "List After Append")
students.extend(["Ameer", "Khalid"])
print(students , "List After Extend")
# List After Extend ['Hassan', 'Ali', ,'Ahmed', 'Omar', 'Sami', 'Zaid', 'haider', 'Ameer', 'Khalid']
students.insert(2, "Yasir")
print(students , "List After Insert")

# Removing Students from the list
students.remove("Omar")
print(students , "List After Removal")

students.pop()
print(students , "List After Pop")  

del students[1]
print(students , "List After Del")

# updating a student name
students[5] = "Zeeshan"
print(students , "List After Update")


# Slicing 
print(students[149:201] , "List After Slicing")
print(students[149:])
print(students[:51] , "List After Slicing from start")


print(students[0:201:3],"List After Slicing with step 2")