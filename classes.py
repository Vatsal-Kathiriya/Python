class Person :
    Name = "Vatsal Kathiriya"
    
    Study = "Information Technology"
    def __init__(self, name, study):
        self.Name = name
        self.Study = study
        print(f"{self.Name} is studying {self.Study}")
    

Name = "Rose"
Study = "Artificial Intelligence"

a = Person("Vatsal", " Information Technology")
b = Person(Name, Study)

