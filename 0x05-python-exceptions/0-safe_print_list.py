#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for idx in my_list:
            if count < x:
                print("{}".format(idx), end="")
                count += 1
            else:
                break
    except IndexError:
        pass
    finally:
        print()
        return count
