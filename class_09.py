# Tuple
# Non mutable type

names = "Hassan" , "Ali", "Omar" , 15 , 20 , 25 , True , False , False
# names[0] = "Mohamed"  # This will raise an error
# print(names)

# it can be used to store constant values
months = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"

# print(months)

cities = {
    (31.5204, 74.3587): "Lahore",
    (24.8607, 67.0011): "Karachi"
}
# print(cities)

# Accessing values
myself = "Hassan" , 16 , True , "Developer" , "Pakistan" , "Islamabad", "Reading" , "Traveling" ,"Coding" , "Gaming"
# print(myself[2])
# print(myself[1 : 4])

# del myself[3]  # This will raise an error   


# nested tuple
nested = (1, 2, 4, ("Hassan"), ("Ali", (8, 7, 6)))
# print(nested)
# print(nested[3])
# print(nested[4][1][2])



tuple1 = (1,2,3 ,4,5,6,7,7,"hassan",9,10)
tuple2 = (4,5,6)
# print(tuple1 * 3)
# print(tuple1 + tuple2)

# if 4 in tuple1:
#     print("Yes 4 is in tuple1")
# else:
#     print("No 4 is not in tuple1")

# print(tuple1.count(7))
# print(tuple1.index("hassan"))

# unpacking tuple 
myself1 = (16 , "Hassan" , True , "Developer" , "Pakistan" , "faisalabad", "Reading" , "Traveling" ,"Coding" , "Gaming")
name , age , is_student , profession , country , city , hobby1 , hobby2 , hobby3 , hobby4 = myself1

print(name)

myself2 = "Hassan",  16, True , "Developer" , "Pakistan" , "faisalabad", "Reading" , "Traveling" ,"Coding" , "Gaming"
name1 , age1 , is_student1 , profession1 , country1 , city1 , hobby1_1 , hobby2_1 , hobby3_1 , hobby4_1 = myself2
print(age1)
print(myself2)