class Company :
    
    Employee = "Jaiwin" # class variable
    
    def __init__(self) :
        print("hello " + self.Employee) 
    
    # classmethod without parameter cls


    @classmethod # classmethod without parameter cls 
    def from_string(cls, nweEmployee) : # classmethod with parameter cls
        cls.Employee = nweEmployee 

    def display(self) :
        print("hello " + self.Employee) 

c1 = Company()
print(Company.Employee)
print() 


c1.from_string("sabbir") # call the classmethod from_string on the object c1
print()


c1.display()
print(Company.Employee) # call the classmethod display on the object c1 

