# OOP 3rd Pillar - Polymorphism
# Polymorphism allows methods to do different things based on the object it is acting upon.

class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

class Cat(Animal):
    def speak(self):
        print("The cat meows")

# for a in (Animal(),Dog(), Cat()):
#     a.speak()




# Example 2
class Cars():
    def brand(self):
        print("This is a car brand")

class BMW(Cars):
    def brand(self):
        print("This is a BMW car")
class Audi(Cars):
    def brand(self):
        print("This is an Audi car")

for c in (Cars(), BMW(), Audi()):
    c.brand()