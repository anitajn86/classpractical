
class library:
    def __init__ (self,member,book):
        self.member=member
        self.book=book

    def borrow(self,book1):
        self.book-=book1
        return (f"Borrowed this {book1} from the library today")
    
    def returnBook(self,book1):
        if book1:
            self.book+=book1
            return(f"I have returned {book1} to the library")
        else:
            return(f"I never borrowed the book in the first place")
        
    def displayBook(self):
        return(f"These {self.book} are available in the library")
    
    def displayMember(self):
        return(f"These {self.member} are the members of the library")
        
