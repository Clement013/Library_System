from enum import Enum


class UserStatus(Enum):
    Terminated = 0
    Active = 1


class BorrowRecordStatus(Enum):
    Borrowing = 1
    Completed = 2


class BookBorrowStatus(Enum):
    Borrowing = 0
    Available = 1


class BookStatus(Enum):
    Deleted = 0
    Active = 1
