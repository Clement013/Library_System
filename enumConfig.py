from enum import Enum


# UserStatus for user Table
class UserStatus(Enum):
    Terminated = 0
    Active = 1


# BorrowRecordStatus for borrowRecord Table
class BorrowRecordStatus(Enum):
    Borrowing = 1
    Completed = 2


# BookBorrowStatus for book Table
class BookBorrowStatus(Enum):
    Borrowing = 0
    Available = 1


# BookStatus for book Table
class BookStatus(Enum):
    Deleted = 0
    Active = 1
