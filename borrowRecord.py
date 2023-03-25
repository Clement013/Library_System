from datetime import datetime, timedelta
import enumConfig as enumConf
import config as conf
from fileDataReadUpdate import *


class BorrowRecord(FileDataReadUpdate):

    def __init__(self):
        """
        Inside the list, the data is stored as:
        [User Id, Book Id, Borrow Date, Return Date, Status (1=borrowing, 2=completed)]
        """
        self.book_records = []
        super().__init__(conf.borrow_record_table, self.book_records)

    # rewrite the data back to the file
    def update_data_to_txt(self):
        self._rewrite_back()

    # check if the user is able to borrow the book
    def check_user_able_to_borrow(self, user_id, membership):
        # define the max borrow and max borrow duration
        max_borrow = conf.normal_max_borrow
        max_borrow_duration = conf.normal_max_borrow_duration
        if membership:
            max_borrow = conf.membership_max_borrow
            max_borrow_duration = conf.membership_max_borrow_duration
        today = datetime.today()
        # check if the user has overdue books
        overdue = filter(
            lambda x: x[0] == user_id and (
                    today.date() - datetime.strptime(x[2], conf.dateString).date()).days > max_borrow_duration and x[
                          4] == str(enumConf.BorrowRecordStatus.Borrowing.value),
            self.book_records)

        if len(list(overdue)) > 0:
            print("The user has borrowed some books and has not returned in time. "
                  "Books cannot be borrowed. User Id: " + user_id, end="\n\n")
            return False

        borrowing_books = list(filter(
            lambda x: x[0] == user_id and x[4] == str(enumConf.BorrowRecordStatus.Borrowing.value),
            self.book_records))
        # check if the user has borrowed the max number of books
        if len(list(borrowing_books)) >= max_borrow:
            print("The user has borrowed the maximum number of books allowed. "
                  "Books cannot be borrowed. User Id: " + user_id, end="\n\n")
            print(f"Current the books borrowed by the user: {['Book Id: ' + a[1] for a in borrowing_books]}",
                  end="\n\n")
            return False
        return True

    # add a new record to the borrow record
    def add_record(self, user_id, book_id):
        self.book_records.append([user_id, book_id,
                                  datetime.strftime(datetime.now(), conf.dateString), "",
                                  str(enumConf.BorrowRecordStatus.Borrowing.value)])
        return True

    # update the book record updated data to list
    def __update_data(self, updated_data):
        for count in range(len(self.book_records)):
            if self.book_records[count][0] == updated_data[0] and self.book_records[count][1] == updated_data[1]:
                self.book_records[count] = updated_data
                return True
        return False

    # find the record by user id and book id
    def find_by_id(self, user_id, book_id):
        for book_record in self.book_records:
            if book_record[0] == user_id and book_record[1] == book_id:
                return book_record
        return None

    # update the record with the return date
    def update_record(self, user_id, book_id, return_date):
        book_record = self.find_by_id(user_id, book_id)
        book_record[3] = datetime.strftime(return_date, conf.dateString)
        book_record[4] = str(enumConf.BorrowRecordStatus.Completed.value)
        return self.__update_data(book_record)
