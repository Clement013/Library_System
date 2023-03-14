from librarySystem import *
from datetime import datetime, timedelta
import atexit


# testing main function
def main_testing():
    a = Users()
    ans = a.find_by_id("S1")

    if ans is None:
        print("Cannot find the user")
    else:
        pass


# define basic function list
basic_function_list = ["Borrow Book process",
                       "Return Book Process",
                       "Exit System"]


# print basic function list
def print_basic_library_function():
    print("\nFunction in this Library System:")
    for i in range(len(basic_function_list)):
        print(f"{i + 1}. {basic_function_list[i]}")


# validate input number
def validate_input_number(input_number):
    try:
        int(input_number)
        return True
    except ValueError:
        return False


system = LibrarySystem()


# exit function
@atexit.register
def exit_func():
    system.ending_process()
    print("\n\nAuto save and exit now...")


# main function
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
            while input_function_no not in (str(i) for i in range(1, len(basic_function_list) + 1)):
                print("Invalid input number value!", end='\n')
                print_basic_library_function()
                input_function_no = input("\nChoose function to proceed (number): ")
                input_function_no = input_function_no.strip()
            # exit the system
            if input_function_no == str(3):
                atexit.unregister(exit_func)
                system.ending_process()
                run = False
                print("\nSaving and Exit now...")
            else:
                # borrow book process
                if input_function_no == str(1):
                    system.borrow_book_main_process()
                # return book process
                elif input_function_no == str(2):
                    system.return_book_main_process()
                else:
                    pass
    except ValueError as e:
        print("Error: {0}".format(e))
        print("System Error.")


if __name__ == '__main__':
    main()
    # main_testing()
