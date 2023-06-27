#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for idx in my_list:
            if isinstance(idx, int):
                if count < x:
                    print("{:d}".format(idx), end="")
                    count += 1
                else:
                    break
    except (IndexError, TypeError):
        pass
    finally:
        print()
        return count
