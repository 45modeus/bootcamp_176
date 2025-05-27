class Librarian:
    def __init__(self, empId, nic, name, address, salary, phone):
        self.empId = empId
        self.nic = nic
        self.name = name
        self.address = address
        self.salary = salary
        self.phone = phone
        
    def register_book(self, shelf, book):
       shelf.add_book(book)
       print(f"Book '{book.title}' has been registered to shelf '{shelf.genre}'.")

    def fetch_book(self, shelf, book):
        shelf.remove_book(book)
        print(f"Book '{book.title}' has been fetched from shelf '{shelf.genre}'.")

    def rent_book(self, shelf, book, customer_name):
        self.fetch_book(shelf, book)
        print(f"Book '{book.title}' of genre '{book.genre}' has been rented to {customer_name}.")

    



    
