class Shelf:
    def __init__(self, id, genre, capacity=100):
        self.id = id
        self.genre = genre
        self.capacity = capacity
        self.books = []

    def add_book(self, book):
        if self.capacity>0: 
            self.books.append(book) #add book to the books list attribute
            self.capacity -= 1 #decrememt capscity
            print(f"Book '{book.title}' has been added to shelf '{self.genre}'.")

    def remove_book(self, book):
        for  item in self.books:
            if item.title==book.title:
                self.books.remove(item)
                self.capacity += 1
                print(f"Book '{book.title}' has been removed from shelf '{self.genre}'.")
                break

    def list_books(self):
        if len(self.books) == 0:
            print("No books available.")
        else:
            print(",".join([book.title for book in self.books]))
            
