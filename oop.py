#learning oop
"""class Car:
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
print(car1.description())"""



class Car:
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
print(car2.accelerate())


