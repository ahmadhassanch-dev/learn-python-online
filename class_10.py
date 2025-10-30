# Loops in python
# FOR loop - While loop

# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# for loop
# for i in [1,2,3,4,5]:
    # print("Hello World", i)

# Example 1  for loop
# for users in ["Hassan" , "Ali" , "Banned User" , "Muhammad" , "Banned User"]:
#     if users == "Banned User":
#         print("Permission denied")
#     else:
#         print("Permission Granted")    

# Example 2 for loop By using break keyword
# for money in [10 , 20 , 50 , 1000 , 500 , 100 , 5000]:
#     if money == 1000:
#         print("I have 1000Rs")
#         break
#     else:
#         print("I don't have 1000Rs")

# By using continue keyword
# for money in [10 , 20 , 50 , 1000 , 500 , 1000 , 5000]:
#     if money == 1000:
#         print("I have 1000Rs")
#         continue
#     else:
#         print("I don't have 1000Rs")

# by using pass keyword

# for i in "Hassan":
#     pass  # it will do nothing and continue the loop


# Increament operator  - decreament operator
# number = 1
# number += 1
# number += 1
# number += 1
# number -= 1
# number -= 1

# print(number)





# While loop
# number = 1
# while number <= 10:
#     print("Number is:", number)
#     number += 1 

# Example 1 while loop
# number = 1
# while number <= 10:
#     print("10 x", number , "=", number * 10)
#     number += 1

# number guessing game using while loop

secret_number = 19
attempts = 1


while attempts <= 20:
    user_input = int(input("Enter a number between 1 - 100: "))
    if user_input <= 0 or user_input >= 100:
        print("Invalid input! Please try again.")
        continue
    if user_input == secret_number:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
        break
    elif user_input < secret_number:
        print("Your number is lower than the secret number! Try again.")
        attempts += 1
    elif user_input > secret_number:
        print("Your number is higher than the secret number! Try again.")
        attempts += 1
else :
    print("You have used all your attempts. Better luck next time!")



