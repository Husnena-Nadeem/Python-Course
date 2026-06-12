class person:
    name="Husnena"
    Lenguage="Python"
    salary=2000000

    def getinfo(self):           #self dana zori ha ok
        print(f"Name is employee is {self.name}\nThe language is {self.Lenguage}.\n The salary is{self.salary}")

        
obj1=person()
obj1.getinfo()

class student:

	#paramaterized constructor
	def __init__(self,fullname): #self is a referance of object 
		print("adding new student :")
		self.name = fullname
          
s1 = student("Abeer")
print(s1.name)
s2 = student("Ali")
print(s2.name)