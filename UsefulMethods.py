x = [1,2,3,4,5,6,7]

print(dir(x))

class a :
    def __init__(self , name , age , address):
        self.age = age 
        self.address = address
        self.name = name
        print("hello world")
        
    def hello(self):
        print("hello") 

a1 = a("vatsal" , 19 , "Amreli") 
a1.hello()
print(a1.__dict__)
print(a.__dict__)

print(help(a))

