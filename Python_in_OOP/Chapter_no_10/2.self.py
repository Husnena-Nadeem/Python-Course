# class person:
#     name="Husnena"
#     Lenguage="Python"
#     salary=2000000

#     def getinfo(self):           #self dana zori ha ok
#         print(f"Name is employee is {self.name}\nThe language is {self.Lenguage}.\n The salary is{self.salary}")

        
# obj1=person()
# obj1.getinfo()
# class Student:
#     # Parameterized Constructor
#     def __init__(self, fullname, marks):
#         print("Adding new student:")
#         self.name = fullname
#         self.marks = marks

#     def welcome(self):
#         print(f"Welcome {self.name}")
#         return self.name


# s1 = Student("Abeer", 85)
# print(s1.name)
# print(s1.marks)

# s2 = Student("Ali", 90)
# print(s2.name)
# print(s2.marks)

# print(s1.welcome())

class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def average(self):
        sum = 0
        for i in self.marks:
            sum += i
        print(f"Hy {self.name} your avarge marks is:",sum/len(self.marks))
            
s1 = students("ali",[90,78,29])
print(s1.name,s1.marks)
s1.average()