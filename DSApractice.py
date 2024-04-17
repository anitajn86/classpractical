class Library:
    def __init__(self, member, num_books):
        self.member = member
        self.num_books = num_books

    def borrow(self, num_books_to_borrow):
        if num_books_to_borrow <= self.num_books:
            self.num_books -= num_books_to_borrow
            return f"Borrowed {num_books_to_borrow} books from the library today"
        else:
            return "Not enough books available to borrow"

    def return_books(self, num_books_to_return):
        self.num_books += num_books_to_return
        return f"Returned {num_books_to_return} books to the library"

    def display_books(self):
        return f"{self.num_books} available books in the library"

    def display_member(self):
        return f"{self.member} is a member of the library"

    def __str__(self):
        return f"Library with {self.member} as member and {self.num_books} books"


User1 = Library('Josh Brolin', 10)
print(User1)
print(User1.borrow(3))
print(User1.display_books())

    
"""To print meaningful information about the Library object,
 you should define a __str__ method within the Library class.
   This method will allow you to customize the string
     representation of the object when it's printed."""
   

