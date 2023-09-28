#!/usr/bin/python3
"""
Get peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of int to find peak from
    Returns: peak of list_of_integers or None
    """
    if not list_of_integers:
        return None

    left, right = 0, len(list_of_integers) - 1
    peak_index = -1

    while left <= right:
        mid = (left + right) // 2

        if list_of_integers[mid] >= list_of_integers[peak_index]:
            peak_index = mid

        if mid == left == right:
            break

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            left = mid + 1
        else:
            right = mid - 1

    return list_of_integers[peak_index]
