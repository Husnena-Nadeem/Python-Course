class teacher:
    def set_name(self):
        self.name=input("Enter the Teacher name:")
        print(f"Enter the name of teacher:{self.name}")
class student:
    def set_name(self):
        self.name=input("Enter the Student name:")
        print(f"Enter te name of studen:{self.name}")
obj1=teacher()
obj1.set_name()
obj2=student()
obj2.set_name()

#without input approch
# class teacher:
#     def set_name(self,name):
#         self.name=name
#         return f"Enter the name of teacher:{self.name}"
# class student:
#     def set_name(self,name):
#         self.name=name
#         return f"Enter te name of studen:{self.name}"
# obj1=teacher()
# print(obj1.set_name("Appppppppp"))
# obj2=student()
# print(obj2.set_name("Hpppppppppp"))