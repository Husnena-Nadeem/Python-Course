class person:
    name="Husnena"
    lenguage="Python"
    salary=200000

    def getinfo(self):           #self dana zori ha ok
        print(f"Name is employee is {self.name}\nThe language is {self.lenguage}.\n The salary is{self.salary}")

obj1=person()
obj1.getinfo()