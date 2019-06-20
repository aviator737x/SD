"""This module contains method for echo"""


def echo(count = 0, args = []):
    """Returns received string"""

    if count == 0:
        return ""
    result = ""
    for arg in args:
        result += arg
        result += " "
    result = result[:len(result) - 1]
    return result
