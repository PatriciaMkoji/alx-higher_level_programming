#!/usr/bin/python3
def no_c(my_string):
    new_mystring = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_mystring = new_mystring + char
    return new_mystring
