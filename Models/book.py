class Book:
    def __init__(self,book_name,writer):
        self.__book_name = book_name
        
    def get_book_name(self):
        return self.__book_name
    
    def set_book_name(self,new_book_name):
        pass