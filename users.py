import config as conf


class Users:

    def __init__(self):
        self.user_detail = []
        self.__read_file()

    def __read_file(self):
        with open(conf.user_table, "r") as file:
            for user in file.readlines():
                list_split = user.split(" | ")
                list_split[-1] = (list_split[-1].split('\n')[0])
                self.user_detail.append(list_split)
        return self.user_detail

    def __rewrite_back(self):
        with open(conf.user_table, "w") as file:
            c = []
            for b in range(len(self.user_detail)):
                c.append((" | ".join(self.user_detail[b])) + "\n")
            file.writelines(c)

    def __update_data(self, updated_data):
        for count in range(len(self.user_detail)):
            if self.user_detail[count][0] == updated_data[0]:
                self.user_detail[count] = updated_data
                self.__rewrite_back()
                return True
        return False

    def find_by_id(self, student_id):
        for a in self.user_detail:
            if a[0] == student_id:
                return a

    def student_valid_to_borrow(self, student_id):
        student = self.find_by_id(student_id)
        if student is not None:
            return student[2] == str(1)
        else:
            return False

    def check_membership(self, student_id):
        student = self.find_by_id(student_id)
        if student is not None:
            return student[4] == str(1)
        else:
            return False

    def update_name(self, student_id, student_name):
        student = self.find_by_id(student_id)
        student[1] = student_name
        return self.__update_data(student)

    def update_status(self, student_id, is_active):
        student = self.find_by_id(student_id)
        student[2] = str(1 if is_active else 0)
        return self.__update_data(student)

    def update_book_borrowed(self, student_id):
        student = self.find_by_id(student_id)
        student[3] = str(1+int(student[3]))
        return self.__update_data(student)

    def update_membership(self, student_id, is_membership):
        student = self.find_by_id(student_id)
        student[4] = str(1 if is_membership else 0)
        return self.__update_data(student)
