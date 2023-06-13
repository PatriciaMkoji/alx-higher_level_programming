#!/usr/bin/python3


"""3. Print a list of integers... in reverse"""
def print_reversed_list_integer(my_list = []):

    reversed_list = my_list[::-1]
    for y in reversed_list:
        print("{:d}".format(y))
