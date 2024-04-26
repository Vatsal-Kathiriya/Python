class MyClass :
    def __init__(self , value):
        print("hello")
        self.value = value 
    def displayandaddition(self , anothervalue):
        self.value = self.value + anothervalue
        print(self.value)
    @staticmethod # static method  
    def static_method_for_additon(val1 , val2):
        print(val1 + val2)

myclass1 = MyClass(10)


myclass1.displayandaddition(10)


myclass1.static_method_for_additon(10 , 20) # one of the method to call static method 

MyClass.static_method_for_additon(10 , 20) # another method to call static method
