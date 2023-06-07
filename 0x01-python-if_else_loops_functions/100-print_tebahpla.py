#!/usr/bin/python3
for digit in range(ord('z'), ord('a') - 1, -1):
    if digit % 2 != 0:
        digit = digit - 32
    print("{:c}".format(digit), end='')
