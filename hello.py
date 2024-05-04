class a :
    def __init__(self , name , age , address) :
        self.name = name
        self.age = age
        self.address = address
    def hello(self) :
        print("hello " + self.name) 
        

obj = a("vatsal" , 21 , "kathmandu") 
obj.hello()
print(obj.name)

# for loop program
for i in range(1,11): 
    print(i)
# for loop program
for i in range(1,11): 
    print(i)

# while loop program
i = 1
while i < 11:
    print(i)
    i += 1

# function program
def sum(a, b):
    return a + b

print(sum(10, 20))

# class program
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

person1 = Person("Vatsal", 21)
person1.print_info()

# list program
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# dictionary program
person = {
    "name": "Vatsal",
    "age": 21,
    "city": "Kathmandu"
}
print(person["name"])

# tuple program
fruits = ("apple", "banana", "cherry")
for fruit in fruits:
    print(fruit)

# set program
fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)

# file program
with open("hello.txt", "w") as file:
    file.write("Hello, world!")

# exception program
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Division by zero error")

# # module program
# import math

# print(math.sqrt(25))

# # package program
# import mypackage

# print(mypackage.myfunction())
