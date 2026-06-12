class person:    
    def getinfo(self):
        self.__name = "Husnena" #private variable
        print(f"Name is emplyee is {self.__name}")
   
    def __salary(self):
        self.salary = 20000 #private method of salary
        print(f"{self.__name} are salary is {self.salary}")
  
    def detali(self):
        self.__salary()

obj1 = person()
obj1.getinfo()
obj1.detali()