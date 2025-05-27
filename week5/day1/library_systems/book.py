class Book:
    def __init__(self,title, author, num_pages, price, isbn,genre): #constructor
        self.title= title
        self.author= author
        self.num_pages= num_pages
        self.price= price
        self.isbn= isbn
        self.genre=genre

    def info(self):
        print(f"Title: {self.title}, Author: {self.author}, Pages: {self.num_pages}, Price: ${self.price}, ISBN: {self.isbn}")
