# 1. Class for representing book data (responsibility: book data)
class BookData:
    def __init__(self, title: str, author: str, isbn: str, price: float = 0.0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"

# 2. Class for saving/managing storage (responsibility: persistence)
class BookRepository:
    def save(self, book: BookData):
        print(f"BookRepository: Saving book '{book.title}' to database.")
        pass

    def get_by_isbn(self, isbn: str) -> BookData:
        print(f"BookRepository: Retrieving book with ISBN '{isbn}'.")
        if isbn == "978-1234567890":
            return BookData("The Clean Coder", "Robert C. Martin", "978-1234567890", 25.50)
        return None

    def update(self, book: BookData):
        print(f"BookRepository: Updating book '{book.title}' in database.")
        pass

# 3. Class for displaying information (responsibility: presentation)
class BookPresenter:
    def display_book_info(self, book: BookData):
        print("\n--- Book Information ---")
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"ISBN: {book.isbn}")
        print(f"Price: ${book.price:.2f}")
        print("------------------------")

# 4. Class for business logic/services (responsibility: business operations)
class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def create_book(self, title: str, author: str, isbn: str, price: float):
        book = BookData(title, author, isbn, price)
        self.repository.save(book)
        return book

    def get_book_details(self, isbn: str):
        book = self.repository.get_by_isbn(isbn)
        if book:
            BookPresenter().display_book_info(book)
        else:
            print(f"Book with ISBN '{isbn}' not found.")

    def change_book_price(self, isbn: str, new_price: float):
        book = self.repository.get_by_isbn(isbn)
        if book:
            book.price = new_price
            self.repository.update(book)
            print(f"Price of '{book.title}' updated to ${new_price:.2f}.")
        else:
            print(f"Could not update price: Book with ISBN '{isbn}' not found.")


# Example Usage
if __name__ == "__main__":
    print("--- Task 1: Class Refactoring (SRP) ---")
    
    book_repo = BookRepository()
    book_service = BookService(book_repo)
    book_presenter = BookPresenter()

    # Creating and saving a book
    new_book = book_service.create_book("Clean Code", "Robert C. Martin", "978-0132350884", 35.99)
    
    # Displaying book information
    book_presenter.display_book_info(new_book)

    # Retrieving and updating a book
    book_service.change_book_price("978-1234567890", 29.99)
    book_service.get_book_details("978-1234567890")
    book_service.get_book_details("non-existent-isbn")