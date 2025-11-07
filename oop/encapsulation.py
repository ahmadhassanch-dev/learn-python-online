# OOP - Object oriented programming
# 1st pillar of OOP is Encapsulation
# Encapsulation 
# We can secure our data by making attributes private

class Car:
    def __init__ (self, speed):
        self._speed = speed  # Protected attribute



    def get_speed(self):
        return self._speed

    def set_speed(self , speed):
        if speed <= 0:
            print("Speed cannot be negative or zero")
        elif speed >= 300:
            print("Speed cannot exceed 300")
        else:
            self._speed = speed
            return self._speed

car = Car(1)
print(car.get_speed())
print(car.set_speed(399))



# Example of a bank
class Bankbalance:
    def __init__ (self, balance):
        self.__balance = balance
    
    def get_balance(self):
        print("Your balance is:", self.__balance)
    

    
    def set_balance(self , balance):
        if balance < 0:
            print("Balance cannot be negative")
        else:
            self.__balance = balance
            print("Your new balance is:", self.__balance)
            
    def deposit(self, amount):
        if amount <= 0 :
            print("Deposit amount must be positive")
        else:
            self.__balance += amount
            print("Your new balance after deposit is:", self.__balance)
            

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Withdraw amount must be positive")
        else:
            self.__balance -= amount
            print("Your new balance after withdrawal is:", self.__balance)

bank = Bankbalance(10000)
print(bank.get_balance())
print(bank.set_balance(5000))
print(bank.deposit(2000))
print(bank.withdraw(5000))
print(bank.withdraw(5000))