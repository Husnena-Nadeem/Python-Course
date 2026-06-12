class acounts:
    def __init__(self,balance,accountNo):
        self.balance = balance
        self.accountNo = accountNo
    def deposite(self,amount):
        self.balance +=amount
        print(f"You balance is {self.balance}")
    def withdraw(self,amount):
        if self.balance >=amount:
            self.balance -= amount
            print(f"You balance is {self.balance}")
        else:
            print("You have not get withdraw amount :")

person1 = acounts(10000,123456)
person1.deposite(5000)
person1.withdraw(2000)
