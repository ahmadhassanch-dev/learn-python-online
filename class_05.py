# If-else statement

# num1 = int(input("Enter a number: "))

# if num1 == "10":
#     print("You Entered 10!")
# elif num1 == 9:
#     print("You Entered 9!")
# elif num1 == 8:
#     print("You Entered 8!")    
# else:
#     print("You did not enter the expected value.")


# print("test print after if statement")



# AND , OR , NOT operatos


# Base value
# age = 45

# if age >= 18 and age <= 65:
#     print("You are eligible to work.")
# else:
#     print("You are not eligible to work.")  
#     print(f"Your age is {age}")  

# if age <= 18 or age >= 65:
#     print("You are not an adult.")
# else:
#     print("You are an adult.")  
#     print(f"Your age is {age}")



# if not (age >= 18 and age <= 65):
#     print("True")
# else:
#     print("False")
#     print(f"Your age is {age}")  


# key_word = "Python1"
# if not (key_word == "python" or key_word == "java"):
#     print("You are not a programmer.")
# else:
#     print("You are a programmer.")  
#     print(f"Your key word is {key_word}")







total_price = int(input("Enter total price: "))

if total_price <= 0:
    print("Invalid price entered.")
elif total_price >= 1000 and total_price < 2000:
    discount = total_price * 0.10
    final_price = total_price - discount
    print(f"You get a 10% discount! Final price is: {final_price}")    
elif total_price >= 2000 and total_price < 3000:
    discount = total_price * 0.20
    final_price = total_price - discount
    print(f"You get a 20% discount! Final price is: {final_price}")
elif total_price >= 3000 and total_price < 5000:
    discount = total_price * 0.30
    final_price = total_price - discount   
    print(f"You get a 30% discount! Final price is: {final_price}")
elif total_price >= 5000:
    discount = total_price * 0.50
    final_price = total_price - discount   
    print(f"You get a 50% discount! Final price is: {final_price}")
else:
    print(f"No discount applied. Final price is: {total_price}")       
