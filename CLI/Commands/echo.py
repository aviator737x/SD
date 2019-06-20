"""This module contains method for echo"""


def echo(count = 0, args = []):
    """Returns received string"""

    if count == 0:
        return ""
    if len(args) > 1:
        print("Too many args")
    else:
        return args[0]
