# without class methord is 
class employee:
    salary=120000
    def show(self):
        print(f"Salary of employee is:{self.salary}")
obj=employee()
obj.salary=10000000
obj.show()

# Class methord can be used in peroty of class atteribute.

# with class methord
class employee:
    salary=120000
    @classmethod
    def show(cls):
        print(f"Salary of employee is:{cls.salary}")
obj=employee()
obj.salary=10000000
obj.show()