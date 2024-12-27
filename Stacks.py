9ipriprintprint*"just tiredclass goodStack:
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
print("The emojis are amazing😭😅")
print("my vs code on the pc is not opening. I don't know what's wrong but I have to commit some code for the day.😭 God help me fix it.")

print ("just tired ")
print ("I am so packed today too. But I hope to start the project soon.")
print("This is the week")
print("just give me a little more time.")
print("hi")

print("😅👀👍🏾😏😭👐🏾💀😒🙄🔥🐾👐🥲🏆 ")
print ("A weirdly lazy person")
print("Hello. We resume work tomorrow.  Today we rest.🤣👍🏾")
print("heyy")
print(" Hey. so busssy with coursework and tests. Be back soon.✌🏾👍🏾 ")
print(" doing maths today😘👍🏾")
print(" rest day😅👍🏾")
print(" ok. back to serious business😁")
print("reading for my software design and engineering test. unable to focus on code🥲.")
print (" Hello, how are you. " )
print (" ola mi hermano ")
print ("blah blah blah ")
print ("hey")
print(" Somehow, my commits to the organization are not shown on the chart😭😭😭😅what should I do?")
print(" just a line of code")
print("hehe.....one day")
print("this us the loc of the day")
print(" another loc of the day ")
print(" a day today was ")
print(" but I have very many lines of code as commits😭😭😅")
print(" good night 😴 🌃 🌙 ✨ world")
print("hmmm")
print("yooo")
print(" it's parteeeeee timee😏🥳🥳🥳")
print("yooo")
print("Christmas was good")
print("yooo...merry Christmas 🎅 🎄 ❤ ")