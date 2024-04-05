class Queue:
    def __init__(self):
        self.Queue=[]

    def enqueue(self,newcar):
        self.Queue.append(newcar)
        print(f"A new car {newcar} has joined the line.")

    def dequeue(self):
        if self.is_empty():
            print("The line has no cars")
        else:
            firstCar=self.Queue.pop(0)
            print(f"The first car in the line,{firstCar} has left the line.")
            return firstCar
        
    def is_empty(self):
        return len(self.Queue)==0
    
    def size(self):
        return len(self.Queue)
    
lines=Queue()

for newcar in ["Chevrolette","Lamborghini","Bentley","Audi","Volkswagen","Bentayga Hybrid"]:
    lines.enqueue(newcar)

print("The cars being removed are:")
lines.dequeue()

lines.size()

print("Also these have been removed")
for _ in range(2):
    lines.dequeue()
    




