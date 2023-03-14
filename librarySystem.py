from datetime import datetime
import time
import config as conf
from book import Book
from borrowRecord import BorrowRecord
from users import Users
from fileDataReadUpdate import *
import enumConfig as enumConf


class LibrarySystem:

    def __init__(self):
        self.users = Users()
        self.borrowRecord = BorrowRecord()
        self.book = Book()
        self.borrow_details = []

    def borrow_book_main_process(self):
        self.borrow_details = []
        FileDataReadUpdate(conf.input_borrow_details, self.borrow_details)
        if not len(self.borrow_details) > 0:
            print("No borrow book details.")
            return
        self.borrow_details.pop(0)
        print("Input borrow details: " + str(self.borrow_details))
        print("Borrow process started!")

        if len(self.borrow_details) > 0:
            for borrow_detail in self.borrow_details:
                time.sleep(1)
                print("Checking valid to borrow...")
                if not self.users.user_valid_to_borrow(borrow_detail[0]):
                    print("The user is invalid to borrow. UserId: " + borrow_detail[0], end="\n\n")
                    time.sleep(1)
                elif not self.book.check_book_available(borrow_detail[1]):
                    print("The book is not available to borrow.  BookId: " + borrow_detail[1], end="\n\n")
                    time.sleep(1)
                else:
                    if self.borrowRecord.check_user_able_to_borrow(
                            borrow_detail[0], self.users.check_membership(borrow_detail[0])):
                        self.borrowRecord.add_record(borrow_detail[0], borrow_detail[1])
                        self.book.update_book_borrow_status(borrow_detail[1], False)
                        print("User Id: " + borrow_detail[0] +
                              " borrow book Id: " + borrow_detail[1] + " successfully.", end="\n\n")
                    else:
                        time.sleep(1)
                        pass

        else:
            print("No borrow book details.")

        print("Borrow process completed!")

    def return_book_main_process(self):
        a = self.users.user_detail
        user_id = input("Enter user ID: ")
        book_id = input("Enter book ID: ")
        self.return_book(user_id, book_id)
        # print("Function No ready!")

    def ending_process(self):
        self.users.update_data_to_txt()
        self.borrowRecord.update_data_to_txt()
        self.book.update_data_to_txt()

    def return_book(self, user_id, book_id):
        borrow_record = self.borrowRecord.find_by_id(user_id, book_id)
        if borrow_record is not None and borrow_record[4] == str(enumConf.BorrowRecordStatus.Borrowing.value):
            self.book.update_book_borrow_status(book_id, True)
            self.borrowRecord.update_record(user_id, book_id, datetime.now())
            user = self.users.find_by_id(user_id)
            if user is not None:
                membership = self.users.check_membership(user_id)
                overdue_days = conf.membership_max_borrow_duration if membership else conf.normal_max_borrow_duration
                days_late = (datetime.today() - datetime.strptime(borrow_record[2],
                                                                  conf.dateString)).days - overdue_days
                if days_late > 0:
                    late_fee = days_late * (
                        conf.membership_charge_overdue if membership else conf.normal_charge_overdue)
                    # user.total_late_fee += late_fee
                    print(f"Please pay RM {late_fee:.2f} for late return.")
                print("Successfully return the book.")

            else:
                print("No user found.")
        else:
            print("No borrow record found for the specified book and user.")
