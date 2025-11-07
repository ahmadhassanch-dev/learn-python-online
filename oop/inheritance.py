# 2nd Pillar of OOP: Inheritance
# Inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).

class Animal:
    def __init__ (self , speaks):
        self.speaks = speaks

    def sound(self , speaks):
        self.speaks = speaks
        print(f"Animal makes a sound: {self.speaks}")
    def get_sound(self):
        return self.speaks

# class Cat(Animal):
#     def info(self):
#         print("I am a cat")


# cat = Cat("Meow")
# print(cat.get_sound())
# print(cat.sound("GRRR..."))
# print(cat.info())

# dog = Animal("Bark")
# print(dog.get_sound())



class Garage:
    def __init__(self , model , year , color):
        self.model = model
        self.year = year
        self.color = color
    
    def info(self):
        print(f"Car Model: {self.model}, Year: {self.year}, Color: {self.color}")

class Car(Garage):
    def start_engine(self):
        print(f"The engine of {self.model} is starting...")
    
    def stop_engine(self):
        print(f"The engine of {self.model} is stopping...")
    
    def get_details(self):
        print(f"Car Details - Model: {self.model}, Year: {self.year}, Color: {self.color}")
    
car1= Car("Toyota" , 2020 , "Red")
car2 = Car("Honda" , 2019 , "Blue")
car3 = Car("Ford" , 2021 , "Black")

print(car1.info())
print(car2.get_details())
print(car3.start_engine())