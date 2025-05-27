from book import Book
from shelf import Shelf
from customer import Customer
from librarian import Librarian

#main program

#create some books a
hp1= Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223, 20.99, "978-0747532699","Fiction")
hp2= Book("Harry Potter and the Chamber of Secrets", "J.K. Rowling", 251, 22.99, "978-0747538493","Fiction")
got= Book("A Game of Thrones", "George R.R. Martin", 694, 29.99, "978-0553103540", "Fiction")
lotr= Book("The Lord of the Rings", "J.R.R. Tolkien", 1178, 39.99, "978-0618640157", "Fiction")
national_geographic= Book("National Geographic: The Photographs", "National Geographic", 256, 24.99, "978-1426211230", "Science")
science_magazine= Book("Science Magazine: The Best of 2020", "AAAS", 200, 19.99, "978-1574441234", "Science")

# Create shelves for different genres
fiction_shelf = Shelf(1, "Fiction", 100)
non_fiction_shelf = Shelf(2, "Science", 200)


#add books to the shelves
fiction_shelf.add_book(hp1)
fiction_shelf.add_book(hp2)
fiction_shelf.add_book(got)
fiction_shelf.add_book(lotr)


# Create a librarian
librarian_alice = Librarian(1, "123456789V", "Alice Smith", "123 Library St", 50000, "0712345678")


# Create customers
customer_john = Customer("John Doe", "john@doe.com")
customer_eric= Customer("Eric Johnson", "eric@ericon.com")

#register books by libarian 
librarian_alice.register_book(non_fiction_shelf, national_geographic)
librarian_alice.register_book(non_fiction_shelf, science_magazine)


print("------- Library System -------")
# List books in the fiction shelf
print("Books in Fiction Shelf:")
fiction_shelf.list_books()

# List books in the non-fiction shelf
print("\nBooks in Non-Fiction Shelf:")
non_fiction_shelf.list_books()

print("---------------")

# Borrow books
customer_john.borrow_book(fiction_shelf, hp1, librarian_alice)
customer_john.borrow_book(fiction_shelf, got, librarian_alice)

customer_eric.borrow_book(non_fiction_shelf,national_geographic, librarian_alice)

# List borrowed books
print("\nJohn's Borrowed Books:")
print(customer_john.get_borrowed_books())
print("\nEric's Borrowed Books:")
print(customer_eric.get_borrowed_books())

#check shleves
print("\nFiction Shelf Books After Borrowing:")
fiction_shelf.list_books()

print("\nNon-Fiction Shelf Books After Borrowing:")
non_fiction_shelf.list_books()

print("---------------")
# Return books
customer_john.return_book(hp1, fiction_shelf, librarian_alice)
customer_eric.return_book(national_geographic, non_fiction_shelf, librarian_alice)

print("---------------")
print('Shelves now after returning')
# List borrowed books after returning
fiction_shelf.list_books()
non_fiction_shelf.list_books()