import config as conf
from fileDataReadUpdate import *
from users import Users


class LibrarySystem:

    def __init__(self):
        self.users = Users()
        self.borrow_details = []

    def borrow_book_main_process(self):
        FileDataReadUpdate(conf.input_borrow_details, self.borrow_details)
        self.borrow_details.pop(0)
        print(self.borrow_details)
        if len(self.borrow_details) > 0:
            for borrow_detail in self.borrow_details:
                if not self.users.user_valid_to_borrow(borrow_detail[0]):
                    print("Invalid user")
                else:
                    print("Valid user")

        else:
            print("No borrow book details.")

        print("Borrow process completed!")

    def return_book_main_process(self):
        a = self.users.user_detail
        print("Return process completed!")

    def ending_process(self):
        self.users.update_data_to_txt()
