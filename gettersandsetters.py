class MyClass :
    
    def __init__(self , name):
        self._name = name  # private variable
        print("hello you are in my class constructor")
        
    
    @property
    def name(self):
        return self._name #_name is private variable
    
    @name.setter
    def name(self , value):
        self._name = value
        
sab = MyClass("Vatsal")  # object creation

print(sab.name)

sab.name = "sabbir"

print(sab.name)
