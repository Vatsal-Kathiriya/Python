class Employee :
    def __init__(self , name, email ): 
        
        print("hii")
        self.name = name     
        self.email = email
        
    @classmethod
    def from_string(cls, string) :
        name, email = string.split(",")
        return cls(name, email)
        
    def display(self) :
        print(self.name,"'s email is",self.email) 


emp1 = Employee.from_string("Vatsal Kathiriya,vatsalkathiriya2@gmail.com")

emp1.display()


# emp1 = Employee.from_string("sabbir")

# emp1.display()



# emp1 = Employee.from_string("sabbir,sabbir@123")

# emp1.display()

    
