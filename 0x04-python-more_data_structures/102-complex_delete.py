#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    del_key = list(map(lambda itm: itm[0], filter(lambda itm: itm[1] == value, a_dictionary.items())))
    for key in del_key:
        del a_dictionary[key]
    return a_dictionary
