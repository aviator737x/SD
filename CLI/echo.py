"""This module contains method for echo"""


def echo(count, args):
    """Returns received string"""

    if len(args) > 1:
        print("Too many args")
    else:
        return args[0]
