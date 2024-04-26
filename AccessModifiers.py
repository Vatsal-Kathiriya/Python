class MyClass :
    def __init__(self) :
        self.public = "I am public"  # public member variable or attribute or field or property or method or function
        self._protected = "I am protected" # protected member variable or attribute or field or property or method or function
        self.__private = "I am private" # private member variable or attribute or field or property or method or function

    def display(self) :
        print(self.public) # calling public member variable or attribute or field or property or method or function
        print(self._protected) # calling protected member variable or attribute or field or property or method or function
        print(self.__private) # calling private member variable or attribute or field or property or method or function
        

obj = MyClass() 
# obj.display()

# obj.public =    "Vatsal" # creating public member variable or attribute or field or property or method or function
# obj._protected = "Sabbir" # creating protected member variable or attribute or field or property or method or function

print(obj.public)
print(obj._protected)
print(obj._MyClass__private) # by using this we can access private member variable or attribute or field or property or method or function

# name mangling in python is used to access private member variable or attribute or field or property or method or function
# print(obj._MyClass__private)


# vwe can directly access with single underscore variable name but not with double underscore variable name


# print(obj.__private) # error : 'MyClass' object has no attribute '__private')
# you can't access private member variable or attribute or field or property or method or function
