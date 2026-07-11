class library:
    def __init__(self,name):
        self.name = name
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def display(self):
        return [f'{book.title} by {book.author}' for book in self.books]

class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author


library = library('JD library')

book1 = book('Harry potter1','JKR')
book2 = book('Harry potter2','JKR')
book3 = book('Harry potter3','JKR')


library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

for book in library.display():
    print(book)
