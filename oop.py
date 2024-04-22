#learning oop
class Car:
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color

    def drive(self):
        print("The car is driving")
    def stop(self):
        print("The car has stopped")
    def description(self):
        return f"The {self.make} is a {self.model}"

car1=Car("chevy","Corvette",2021,"blue")
print(car1.model)

car1.drive()
print(car1.description())



"""class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def accelerate(self):
        return f"The {self.model} is accelerating"

    def brake(self):
        print("The" + self.make+ "is braking")
    
car1=Car("Bumpy","Chevrolette",2000)
print(car1.make)
print(car1.accelerate())
car1.brake()

car2=Car("Shady","Monster truck",2006)
car2.brake()
print(car2.accelerate())"""

class BankAccount:
    def __init__(self,accountNumber,balance=0):
        self.accountNumber=accountNumber
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        return f"Deposited {amount} into account {self.accountNumber}. New balance is {self.balance}"
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"You have withdrawn {amount}.Your new balance is {self.balance}")
        else:
            print("Insufficient funds")

    def displayBalance(self):
        print(f"Account {self.accountNumber} has a balance of {self.balance}")

#super() is a built in function used to access methods from the parent class within
        #a subclass
class SavingsAccount(BankAccount):
    def __init__(self,accountNumber,interestRate,balance=0):
        super().__init__(self,accountNumber,balance)
        self.interestRate=interestRate

    def addInterest(self):
        interest=self.balance*(self.interestRate)
        self.deposit(interest)
        print(f"Added interest to account {self.accountNumber}. The new balance is {interest}")

class checkingAccount(BankAccount):
    def __init__(self,accountNumber,transactionFee,balance=0):
        super().__init__(self,accountNumber,balance)
        self.transactionFee=transactionFee

    def DeducttransFee(self):
        self.withdraw(self.transactionFee)
        print(f"Deducted {self.transactionFee} from account {self.accountNumber}. New balance is {self.balance}")


customer1=BankAccount('C678990',4000)
print(customer1.deposit(5000))
customer1.withdraw(2000)
customer1.displayBalance()

customer2=SavingsAccount("B776570", interestRate=2.4)
print(customer2.deposit(1000))
customer2.addInterest()
customer2.DeducttransFee()






