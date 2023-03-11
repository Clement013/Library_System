from librarySystem import *
from datetime import datetime, timedelta
import atexit


def main_testing():
    a = Users()
    ans = a.find_by_id("S1")
    # today = datetime.today()
    # date_time_converted = datetime.strptime("2023/2/24 12:30", "%Y/%m/%d %H:%M")
    # print((today.date() - date_time_converted.date()).days)

    if ans is None:
        print("Cannot find the user")

    else:
        pass

        # print(ans)
        # print(a.update_name(ans[0], "Clement Tai"))
        # print(a.user_detail)
        # a.update_membership(ans[0], False)
        # print(a.check_membership(ans[0]))


basic_function_list = ["Borrow Book process",
                       "Return Book Process",
                       "Join Membership Process",
                       "Exit System"]


def print_basic_library_function():
    print("\nFunction in this Library System:")
    for i in range(len(basic_function_list)):
        print(f"{i + 1}. {basic_function_list[i]}")


def validate_input_number(input_number):
    try:
        int(input_number)
        return True
    except ValueError:
        return False


system = LibrarySystem()


@atexit.register
def exit_func():
    system.ending_process()
    print("\n\nAuto save and exit now...")


def main():
    try:
        print("=================================")
        print("Welcome to Library System !")
        print("=================================")

        run = True
        while run:
            print_basic_library_function()
            input_function_no = input("\nChoose function to proceed (number): ")
            input_function_no = input_function_no.strip()
            # while the input not equal 1,2,3,4
            while input_function_no not in (str(i) for i in range(1, len(basic_function_list)+1)):
                print("Invalid input number value!", end='\n')
                print_basic_library_function()
                input_function_no = input("\nChoose function to proceed (number): ")
                input_function_no = input_function_no.strip()
            if input_function_no == str(4):
                atexit.unregister(exit_func)
                system.ending_process()
                run = False
                print("\nSaving and Exit now...")
            else:
                if input_function_no == str(1):
                    system.borrow_book_main_process()
                elif input_function_no == str(2):
                    system.return_book_main_process()
                elif input_function_no == str(3):
                    system.join_membership_main_process()
                else:
                    pass
    except ValueError as e:
        print("Error: {0}".format(e))
        print("System Error.")


if __name__ == '__main__':
    main()
    # main_testing()
