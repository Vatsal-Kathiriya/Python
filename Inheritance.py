class MyClass :
    def __init__(self , name):
        self.name = name 
    def display(self):
        print("hello " + self.name)

class MyClass2(MyClass):
    def __init__(self , name , age):
        super().__init__(name) # calling parent class constructor
        self.age = age

    def display2(self):
        print("hello " + self.name + " " + self.age)
        
myclass1 = MyClass("vatsal")
myclass1.display()

myclass2 = MyClass2("sabbir" , "20") # creating object of child class
myclass2.display2()

