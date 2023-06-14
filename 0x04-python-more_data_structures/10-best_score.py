#!/usr/bin/python3
def best_score(a_dictionary):
    y = 0
    z = None
    if a_dictionary:
        for i in a_dictionary:
            if a_dictionary[i] > y:
                y = a_dictionary[i]
                z = i
    return z
