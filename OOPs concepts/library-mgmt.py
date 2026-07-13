class books:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def display(self):
        print(f'Author : {self.author}')
        print(f'Title : {self.title}')

class library:
    def __init__(self):
        self.books = []

    # add book
    def add_books(self,book):
        self.books.append(book)
        print(f'The book : {book.title} added successfully ! \n')    

    # remove book
    def remove_books(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f'{title} removed successfully ! \n')
                return
        print('Book not found. \n')

    # search book
    def search_books(self,title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print('Book found')
                book.display()
                print()
                return
        print('Book not found. \n')
            
    # display all books
    def display_books(self):
        if not self.books:
            print('Library is empty.')
        else:
            print('The books in the library are : ')
            for book in self.books:
                book.display()
                print()

# Creating Library object
library = library()

# Creating Book objects
book2 = books("Atomic Habits", "James Clear")
book3 = books("Python Crash Course", "Eric Matthes")
book1 = books("The Alchemist", "Paulo Coelho")

# add books
library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

# Display all books
library.display_books()

# Search a book
library.search_books("Atomic Habits")

# Remove a book
library.remove_books("The Alchemist")

# Display remaining books
library.display_books()