class person:
    name="Husnena"
    Lenguage="Python"
    salary=2000000

    def getinfo(self):           #self dana zori ha ok
        print(f"Name is employee is {self.name}\nThe language is {self.Lenguage}.\n The salary is{self.salary}")
    

    @staticmethod
    def good():
        print("Good Morning.")
        
obj1=person()
obj1.getinfo()
obj1.good()
obj2=person()
