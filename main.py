from LibrarySystem import *


def main_testing():
    a = Users()
    ans = a.find_by_id("S1")

    if ans is None:
        print("Cannot find the user")

    else:
        pass

        # print(ans)
        # print(a.update_name(ans[0], "Clement Tai"))
        # print(a.user_detail)
        # a.update_membership(ans[0], False)
        # print(a.check_membership(ans[0]))


def main():
    system = LibrarySystem()
    print("=================================")
    print("Welcome to Library System !")
    print("=================================")

    run = True
    while run:
        print("1. Borrow Book process")
        print("2. Return Book Process")
        print("3. Exit")
        input1 = input("Choose function process (number): ")
        while input1 != str(1) and input1 != str(2) and input1 != str(3):
            print("Wrong input, please enter a valid input!")
            print("1. Borrow Book process")
            print("2. Return Book Process")
            print("3. Exit")
            input1 = input("Choose function process (number): ")
            pass
        if input1 == str(3):
            system.ending_process()
            run = False
            print("Exit now...")
        else:
            if input1 == str(1):
                system.borrow_book_main_process()

            elif input1 == str(2):
                system.return_book_main_process()
            else:
                pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
