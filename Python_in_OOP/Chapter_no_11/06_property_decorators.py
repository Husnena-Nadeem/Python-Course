
# class employee:
#     salary=120000
#     def show(self):
#         print(f"Salary of employee is:{self.salary}")
#     @property
#     def name(self):
#         return f"{self.firstname,self.lastname}"
#     @name.setter
#     def name(self,value):
#         self.firstname=value.split(" ")[0]
#         self.lastname=value.split(" ")[1]
    
# obj=employee()
# obj.salary=10000000
# obj.name="Husnena Nadeem"
# print(obj.name)
# print(obj.firstname)
# print(obj.lastname)
# obj.show()


class employee:
    def __init__(self,name,salary):
        self._name=name
        self._salary=salary
    
