from datetime import datetime, timedelta
import enumConfig as enumConf
import config as conf
from fileDataReadUpdate import *


class BorrowRecord(FileDataReadUpdate):

    def __init__(self):
        """
        [User Id, Book Id, Borrow Date, Return Date, Status (1=borrowing, 2=completed)]
        """
        self.book_records = []
        super().__init__(conf.borrow_record_table, self.book_records)

    def update_data_to_txt(self):
        self._rewrite_back()

    def check_user_able_to_borrow(self, user_id, membership):
        max_borrow = conf.normal_max_borrow
        max_borrow_duration = conf.normal_max_borrow_duration
        if membership:
            max_borrow = conf.membership_max_borrow
            max_borrow_duration = conf.membership_max_borrow_duration
        today = datetime.today()
        overdue = filter(
            lambda x: x[0] == user_id and (
                    today.date() - datetime.strptime(x[2], conf.dateString).date()).days > max_borrow_duration and x[
                          4] == str(enumConf.BorrowRecordStatus.Borrowing.value),
            self.book_records)

        if len(list(overdue)) > 0:
            print("The user has borrowed some books and has not returned in time. "
                  "Books cannot be borrowed. User Id: " + user_id)
            return False

        borrowing_books = list(filter(
            lambda x: x[0] == user_id and x[4] == str(enumConf.BorrowRecordStatus.Borrowing.value),
            self.book_records))

        if len(list(borrowing_books)) >= max_borrow:
            print("The user has borrowed the maximum number of books allowed. "
                  "Books cannot be borrowed. User Id: " + user_id)
            print(f"Current the books borrowed by the user: {['Book Id: ' + a[1] for a in borrowing_books]}",
                  end="\n\n")
            return False
        return True

    def add_record(self, user_id, book_id):
        self.book_records.append([user_id, book_id,
                                  datetime.strftime(datetime.now(), conf.dateString), "",
                                  str(enumConf.BorrowRecordStatus.Borrowing.value)])
        return True