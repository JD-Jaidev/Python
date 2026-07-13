class book:
    def __init__(self,title,page):
        self.title = title
        self.page = page

    def __str__(self):
        return self.title

    def __len__(self):
        return self.page
    
book = book('Harry potter', 250)

print(f'The book name is : {book}')

print(f'The number of pages in the book is : {len(book)}')