class goodStack:
    def __init__(self):
        self.stack=[]

    def push(self,newElement):
        self.stack.append(newElement)
        print(f"The new element in the stack is {newElement}")

    def pop(self):
        if self.is_empty():
            print("The stack has no elements currently")
        else:
            removedElement=self.stack.pop(len(self.stack)-1)
            print(f"The element {removedElement} at the top of the stack has been removed.")
            return removedElement
        
    def is_empty(self):
        if len(self.stack)==0:
            print("There are no elements in the stack")
        else:
            print(len(self.stack))


stack=goodStack()

for newElement in ["book","cup","plate","fish","chicken"]:
    stack.push(newElement)
    
print("The items being removed from the stack are:")
stack.pop()

stack.is_empty()


print("eid is done......and now back to exams")
print("mbu Hello world🤣🤣")
print("i love code with emojis🤣😏😎")