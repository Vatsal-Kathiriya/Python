class Person():
    def __init__(self, name, birth_day):
        self.name = name
        self.birth_day = birth_day

    @classmethod
    def from_birth_year(cls, String):
        return cls(String.split("_")[0],String.split("_")[1])


person = Person.from_birth_year("Vatsal Kathiriya_24/12/2004")
print(person.name,"'s birth day is ", person.birth_day)