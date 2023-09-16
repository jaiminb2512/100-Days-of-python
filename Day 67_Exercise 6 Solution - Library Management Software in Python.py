# Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesnt persist the books after the program is stopped!

class Library:
    def __init__(self):
        self.nobook = 0
        self.books = []
        
    def Addbook(self,book):
        self.books.append(book)
        self.nobook = len(self.books)
        
    def infobook(self):
        print(f"The no of books is {self.nobook}")      
        for book in self.books:
            print(book)
            
            
b1 = Library() 
b1.Addbook("Use of truth")
b1.Addbook("Jaimin")
b1.infobook()



