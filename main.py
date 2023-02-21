from users import *


def main():
    a = Users()
    ans = a.find_by_id("S1")

    if ans is None:
        print("Cannot find the user")
    else:
        # print(ans)
        #print(a.update_name(ans[0], "Clement Tai"))
        # print(a.user_detail)
        # a.update_membership(ans[0], False)
        # print(a.check_membership(ans[0]))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
