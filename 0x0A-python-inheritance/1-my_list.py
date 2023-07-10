#!/usr/bin/python3
class MyList(list):
    """
    a subclass that inherits from list
    """

    def print_sorted(self):
        """
        prints the list, but in sorted order

        Args:
        self: calss self

        Returns:
            prints the list in sorted manner
        """
        print(sorted(self))
