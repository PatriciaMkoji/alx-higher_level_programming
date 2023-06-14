#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    result_value = list(map(lambda symbol: roman_values[symbol], roman_string))
    total_value = 0
    prev_value = 0
    for value in reversed(result_value):
        if value < prev_value:
            total_value -= value
        else:
            total_value += value
        prev_value = value
    return total_value
