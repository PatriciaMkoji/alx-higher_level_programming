#!/usr/bin/python3
"""
class doc
My int
"""


class MyInt(int):
    """
    converts int == and !=
    """
    def __eq__(self, num):
        """ Change == to !="""
        return int(self) != int(num)

    def __ne__(self, num):
        """ Change != to =="""
        return int(self) == int(num)
