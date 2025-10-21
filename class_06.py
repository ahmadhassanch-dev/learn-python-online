# functions in python

# def sum(): 
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     total = num1 + num2
#     print(f"{num1} + {num2} = {total}")

# sum()


# def subtract(num1, num2):
#     def multiply(num1, num2):
#         mul = num1 * num2
#         print(f"{num1} * {num2} = {mul}")
#     multiply(num1, num2)

#     minus = num1 - num2
#     print(f"{num1} - {num2} = {minus}")

# subtract(10, 5)



#  Assignment 3: Battery Health Analyzer
#  Objective: To analyze phone battery status based on percentage and charging condition.
#  Requirements:
#  1. Ask the user for current battery percentage (0–100) and whether the phone is charging
#  (yes/no).
#  2. Use only if-else, logical, and comparison operators to print the correct message.
#  Formula:
#  Logical conditions used for decision making (e.g., If (Battery ≤ 10) and (Charging == 'no')).
#  Conditions:- Battery ≤ 10 and not charging →  Battery Critical – Plug in immediately!- Battery ≤ 10 and charging →  Charging started just in time!- 10 < Battery ≤ 30 and not charging → 
#  Battery Low – Consider charging soon.- 30 < Battery ≤ 60 and not charging →  Battery OK – Moderate usage allowed.- 60 < Battery ≤ 90 and charging →  Battery good – you can unplug soon.- Battery > 90 and charging →  Battery Full – Unplug charger to save energy.- Otherwise →  Battery sufficient – all good!


def battery_analyzer():
    battery = int(input("Enter your current battery percentage (0 - 100): "))
    is_charging = input("Is your phone/laptop is charging? (yes/no): ").lower()
    
    if battery <= 0 or battery > 100:
        print("Invalid battery percentage.")
    elif battery <= 10 and is_charging == "no":
        print("Battery Critical  Plug in immediately!")
    elif battery <= 10 and is_charging == "yes" :
        print("Charging started just in time!")
    elif battery > 10 and battery <=30 and is_charging == "no":
        print("Battery Low Consider charging soon.")
    elif battery > 10 and battery <=30 and is_charging == " yes":
        print("Battery Low  Charging started just in time!")
    elif battery > 30 and battery <= 60 and is_charging == "no":
        print("Battery OK  Moderate usage allowed.")
    elif battery > 30 and battery <= 60 and is_charging == "yes":
        print("Battery OK  Moderate usage allowed.")
    elif battery > 60 and battery <=90 and is_charging == "no":
        print("Battery good you can plug in soon.")
    elif battery > 60 and battery <=90 and is_charging == "yes":
        print("Battery good you can unplug soon.")
    elif battery > 90 and battery <= 100 and is_charging == "yes":
        print("Battery Full  Unplug charger to save energy.")
    else:
        print("Battery sufficient all good!")

battery_analyzer()