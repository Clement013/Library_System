import config as conf
from fileDataReadUpdate import *
from enumConfig import UserStatus


class Users(FileDataReadUpdate):

    def __init__(self):
        """
        [Id, Name, Status (0=Terminated, 1=Active),
        Total Number of book borrowed, Membership (0=not member, 1=is member)]
        """
        self.user_detail = []
        super().__init__(conf.user_table, self.user_detail)

    def update_data_to_txt(self):
        self._rewrite_back()

    def __update_data(self, updated_data):
        for count in range(len(self.user_detail)):
            if self.user_detail[count][0] == updated_data[0]:
                self.user_detail[count] = updated_data
                return True
        return False

    # read
    def find_by_id(self, user_id):
        for user in self.user_detail:
            if user[0] == user_id:
                return user
        return None

    def user_valid_to_borrow(self, user_id):
        user = self.find_by_id(user_id)
        if user is not None:
            return user[2] == str(UserStatus.Active.value)
        else:
            return False

    def check_membership(self, user_id):
        student = self.find_by_id(user_id)
        if student is not None:
            return bool(int(student[4]))
        else:
            return False

    def update_name(self, user_id, user_name):
        user = self.find_by_id(user_id)
        user[1] = user_name
        return self.__update_data(user)

    def update_status(self, user_id, is_active: bool):
        user = self.find_by_id(user_id)
        user[2] = str(1 if is_active else 0)
        return self.__update_data(user)

    def update_book_borrowed(self, user_id):
        user = self.find_by_id(user_id)
        user[3] = str(1 + int(user[3]))
        return self.__update_data(user)

    def update_membership(self, user_id, is_membership: bool):
        user = self.find_by_id(user_id)
        user[4] = str(1 if is_membership else 0)
        return self.__update_data(user)
