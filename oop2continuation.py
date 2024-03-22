class Library:
    def __init__(self,member,book):
        self.member=member
        self.book=book

    def borrowBook(self,newBook=""):
        self.book-=newBook
        print(f"Borrowed this new {newBook} from the library today")

    def returnBook(self,newBook):
        if newBook:
            self.book+=newBook
            print(f"I will return this {newBook} to the library tomorrow")
        else:
            print("I don't have any book that i should be returning")
 
    def displayBook(self):
        print(f"This {self.book} is available at the library")

"""class Member(Library):
    def __init__(self,name):
        super().__init__(self,member,book)
        self.name=name

    def borrowBook(self):
        self.name(self.book)"""

member1=Library("anita",'Cinderella')
member1.borrowBook("Milan & Italy")