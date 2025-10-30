#init methord like a constructor.
#They can call atomaticaly in creation function.

class person:
    name="Husnena"
    Lenguage="Python"
    salary=2000000

    def getinfo(self):           #self dana zori ha ok.
        print(f"Name is employee is {self.name}\nThe language is {self.Lenguage}.\n The salary is{self.salary}")
    def __init__(self,name,Lenguage,salary):           #This is dusnder methord. 
        self.name=name
        self.Lenguage=Lenguage
        self.salary=salary
        print("Thie is init methord in python this is atomatic call in creating object.")
        
obj1=person("Husnena","C++",120000)
print(obj1.name,obj1.Lenguage,obj1.salary)
obj1.getinfo()

