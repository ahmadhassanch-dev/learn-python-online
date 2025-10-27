# New type
# Dictionary - Mutable Type
# In context of other languages: HashMap, Object

students = {
    "name" : "Hassan",
    "age" : 17
}
# print(students, "Original Dictionary")

# Incomparizon to lists

car1 = ["Nissan", "Skyline", 2015]

cars = {
    "company" : "Nissan",
    "model" : "Skyline",
    "year" : 2015
}
# print(cars, "Car Dictionary")

# Adding new key-value
cars["color"] = "White-blue"

# print(cars , "Dictionary After Adding new key-value")

# Updating value
cars["year"] = 2018
# print(cars , "Dictionary After Updating value")

# Removing key-value
del cars["year"]
# print(cars , "Dictionary After Deleting key-value")

print()

# print(cars)

# Accessing value

# print(cars["model"])
# print(cars["company"])

# Nested Dictionary
car_dealership ={
    "Nissan": {
        "company" : "Nissan",
        "model" : "Skyline",
        "year" : 2015
    },
    "Toyota": {
        "company" : "Toyota",
        "model" : "Supra",
        "year" : 2020
    },
    "Mazda": {
        "company" : "Mazda",
        "model" : "RX-7",
        "year" : 1998
    }
}
# print(car_dealership)
# print()
# print(car_dealership["Toyota"])
# print()
# print(car_dealership["Nissan"]["model"])


# Checking if key exists
if "Nissan" in car_dealership:
    print("Available")
    car_dealership["Mehran"] = {
        "company" : "Suzuki",
        "model" : "Mehran",
        "year" : 2005}
    print(car_dealership["Mehran"])


elif "Honda" in car_dealership:
    print("Available")
    car_dealership["Honda"] = {
        "company" : "Honda",
        "model" : "Civic",
        "year" : 2020}
    print(car_dealership["Honda"])

else:
    print("Not Available")