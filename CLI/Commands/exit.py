"""This module contains a method for exit"""


class ExitException(Exception):
    pass


def exit(*args):
    """Stops CLI interpretation"""
    raise ExitException
