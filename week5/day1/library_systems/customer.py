class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.borrowed_books = []

    def borrow_book(self, shelf, book, librarian):
        if book not in self.borrowed_books:
            self.borrowed_books.append(book)
            librarian.rent_book(shelf, book, self.name)
            print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book, shelf,librarian):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            librarian.register_book(shelf,book)  
            print(f"{self.name} returned '{book.title}'.")

    def get_borrowed_books(self):
        return (",".join([book.title for book in self.borrowed_books]))