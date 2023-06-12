#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    multiplier = []
    for y in range(len(my_list)):
        if my_list[y] % 2 == 0:
            multiplier.append(True)
        else:
            multiplier.append(False)
    return (multiplier)
