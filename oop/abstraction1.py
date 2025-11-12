# Abstraction
from abc import ABC , abstractmethod

class Vehecle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehecle):
    def start_engine(self):
        print("Car engine started")

class Bike(Vehecle):
    def start_engine(self):
        print("Bike engine started")

# for a in (Car() , Bike()):
#     a.start_engine()



# Example OOPs all pillars
# banking system
class Bank(ABC): # abstraction
    def __init__(self , client_name , balance):
        self.__client_name = client_name
        self.__balance = balance  # encapsulation

    def deposit(self , amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance is {self.__balance}")

    def withdraw(self , amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}")
    def get_balance(self):
        @abstractmethod
        def display_balance(self ):
            pass

class SavingsAccount(Bank): # inheritance
    def savings_interest(self , rate):
        interest = self.__balance * rate / 100
        self.__balance += interest
        print(f"Added interest {interest}. New balance is {self.__balance}")
 
 
    def display_balance(self , balance):
        self.__balance = balance
        print(f"Balance is {self.__balance}")


class CurrentAccount(Bank):
    def overdraft(self , amount):
        self.__balance -= amount
        print(f"Overdrafted {amount}. New balance is {self.__balance}")
    def display_balance(self , balance):
        self.__balance = balance
        print(f"Balance is {self.__balance}")

client1 = SavingsAccount("Alice" , 1000) # polymorphism
client2 = SavingsAccount("Bob" , 2000)
client3 = CurrentAccount("Charlie" , 3000)

for client in (client1 , client2 , client3):
    client.deposit(500)
    client.withdraw(200)
    client.display_balance(client._Bank__balance)
    