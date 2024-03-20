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

#implementing stacks
class Stack(object):
    def __init__(self):
        self.item=[]

    def push(self,item):
        #push items to last index...return:None
        self.item.append(item)

    def pop(self,item):
        #this will remove last item...return:None
        self.item.pop(item)
        

    def peek(self):
        #allows us to see the last elements....return:Last item
        if self.item:
            return self.item[-1]
        else:
            return None
        
    def size(self):
        if self.item:
            return len(self.item)
        else:
            return None
        
    def isEmpty(self):
        #tells if stack is empty or not...return:Boolean value
        if self.item==[]:
            return True
        else:
            return False

#if __name__=="__main__":

item=[3,4,5,7,6,8,9,]
Stack.pop([0])
#print("Pop", element)
"""Stack.push[1]
Stack.push[2]
print(Stack.size())
print(Stack.peek())"""