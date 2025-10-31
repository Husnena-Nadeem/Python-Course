class compney:
    compney="tek"
class   lenguage(compney):
    lenguage="Python"
    salary=1200000
    def deflo_info(self):
        print(f"Conpney name: {self.compney},    working lenguage is  {self.lenguage}   Salary of employee is {self.salary}")
class person(lenguage):

    def __init__(self):
        self.name=input("Enter Your name:")
        self.age=int(input("Enter the age is person:"))
        
    def detaile(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Company: {self.compney}, Language: {self.lenguage}, Salary: {self.salary}")

obj1=person()
print(obj1.detaile())      
