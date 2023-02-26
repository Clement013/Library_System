class FileDataReadUpdate(object):
    """
    This class is used to read and update data from the txt file
    """
    def __init__(self, path_data, list_detail: list):
        self.path_data = path_data
        self.list_detail = list_detail
        self.__read_file()

    def __read_file(self):
        with open(self.path_data, "r") as file:
            for user in file.readlines():
                list_split = user.strip().split(" | ")
                self.list_detail.append(list_split)
        return self.list_detail

    def _rewrite_back(self):
        with open(self.path_data, "w") as file:
            c = []
            for b in range(len(self.list_detail)):
                c.append((" | ".join(self.list_detail[b])) + "\n")
            file.writelines(c)
