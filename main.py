from librarySystem import *


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


def print_basic_library_function():
    print("\nFunction in this Library System:")
    print("1. Borrow Book process")
    print("2. Return Book Process")
    print("3. Exit System")


def validate_input_number(input_number):
    try:
        int(input_number)
        return True
    except ValueError:
        return False


def main():
    try:
        system = LibrarySystem()
        print("=================================")
        print("Welcome to Library System !")
        print("=================================")

        run = True
        while run:
            print_basic_library_function()
            input_function_no = input("\nChoose function to proceed (number): ")
            # while the input not equal 1,2,3
            while input_function_no.strip() not in (str(i) for i in range(1, 4)):
                print("Invalid input number value!", end='\n')
                print_basic_library_function()
                input_function_no = input("\nChoose function to proceed (number): ")

            if input_function_no.strip() == str(3):
                system.ending_process()
                run = False
                print("\nExit now...")
            else:
                if input_function_no.strip() == str(1):
                    system.borrow_book_main_process()

                elif input_function_no.strip() == str(2):
                    system.return_book_main_process()
                else:
                    pass
    except ValueError:
        print("System Error.")


if __name__ == '__main__':
    main()
    # main_testing()
