#!/usr/bin/python3
"""
module docs
"""
import sys


""" Initialization of metrics variables """
total_file_size = 0
status_code_counts = {}

# Define a function to print the statistics


def print_statistics():
    """
    Print the metrics statistics.

    prints the total file size & number of lines for each status code.
    """
    print("Total file size: {}".format(total_file_size))
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        print("{}: {}".format(status_code, count))


try:
    """ Read stdin line by line """
    for i, line in enumerate(sys.stdin, 1):
        # Parse the input line
        parts = line.strip().split(" ")
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] = status_code_counts.get(status_code, 0) + 1

        # Print statistics every 10 lines
        if i % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()
