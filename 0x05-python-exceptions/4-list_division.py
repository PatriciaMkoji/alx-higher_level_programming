#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for idx in range(list_length):
            try:
                dividend = my_list_1[idx]
                divisor = my_list_2[idx]
                if isinstance(dividend, (int, float)) and isinstance(divisor, (int, float)):
                    try:
                        division = dividend / divisor
                        result.append(division)
                    except ZeroDivisionError:
                        result.append(0)
                        print("division by 0")
                else:
                    result.append(0)
                    print("wrong type")
            except IndexError:
                result.append(0)
                print("out of range")
    finally:
        return result
