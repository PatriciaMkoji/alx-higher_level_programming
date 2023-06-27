#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for element in my_list:
            if isinstance(element, int):
                if count < x:
                    print("{:d}".format(element), end="")
                    count += 1
                else:
                    break
                except IndexError:
                    pass
                finally:
                    print()
                    return count
