from Models.book import Book

class BookService:
    def create_book(self,book_name):
        return Book(book_name)

    def delete_book(self,book_name):
        pass