class employee:
    compny="TECK"
    def conp(self):
        print(f"The compney of{self.compny}")


class programer(employee):
    name="Husnena"
    def info(self):
        print(f"The name of employee is: {self.name} The compney of{self.compny}")
        
person1=programer()
print(person1.info())