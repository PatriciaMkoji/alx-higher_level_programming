#!/usr/bin/python3
def fizzbuzz():
    for idx in range(1, 101):
        if (idx % 3 == 0 and idx % 5 != 0):
            print("Fizz", end=' ')
        elif (idx % 5 == 0 and idx % 3 != 0):
            print("Buzz", end=' ')
        elif (idx % 3 == 0 and idx % 5 == 0):
            print("FizzBuzz", end=' ')
        else:
            print("{:d}".format(idx), end=' ')
