import enumConfig as enumConf
import config as conf
from fileDataReadUpdate import *


class Book(FileDataReadUpdate):
    def __init__(self):
        """
        [Id, Name, Borrow Status (0=borrowing, 1=available),Book Status(0=not in library(deleted),1=In library)]
        """
        self.books = []
        super().__init__(conf.book_table, self.books)

    # rewrite the data back to the file
    def update_data_to_txt(self):
        self._rewrite_back()

    # update the data in the list
    def __update_data(self, updated_data):
        for count in range(len(self.books)):
            if self.books[count][0] == updated_data[0]:
                self.books[count] = updated_data
                return True
        return False

    # find the book by id
    def find_by_id(self, book_id):
        for book in self.books:
            if book[0] == book_id:
                return book
        return None

    # check if the book is in the library
    def check_book_exist(self, book_id):
        book = self.find_by_id(book_id)
        if book is not None:
            return book[3] == str(enumConf.BookStatus.Active.value)
        else:
            return False

    # check if the book is available
    def check_book_available(self, book_id):
        book = self.find_by_id(book_id)
        if book is not None:
            return book[2] == str(enumConf.BookBorrowStatus.Available.value)
        else:
            return False

    # get the book name
    def get_book_name(self, book_id):
        book = self.find_by_id(book_id)
        if book is not None:
            return book[1]
        else:
            return None

    # update the book borrow status
    def update_book_borrow_status(self, book_id, is_available: bool):
        book = self.find_by_id(book_id)
        book[2] = str(enumConf.BookBorrowStatus.Available.value if is_available else enumConf.BookBorrowStatus.Borrowing.value)
        return self.__update_data(book)
