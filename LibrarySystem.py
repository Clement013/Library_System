from users import *


class LibrarySystem:

    def __init__(self):
        self.users = Users()

    def borrow_book_main_process(self):
        a = self.users.user_detail

    def return_book_main_process(self):
        pass

    def ending_process(self):
        self.users.update_data_to_txt()
