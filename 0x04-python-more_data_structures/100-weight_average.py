#!/usr/bin/python3
def weight_average(my_list):
    if not my_list:
        return 0

    tot_summation = sum(map(lambda x: x[0] * x[1], my_list))
    tot_weight = sum(map(lambda x: x[1], my_list))

    return tot_summation / tot_weight
