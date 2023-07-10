#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    checks if  object is an instance of a class it inherited from

    Args:
        obj:the object to be looked into

    Return:
        True if object is instance of a class
        False if its not
    """
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
