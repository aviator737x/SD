"""This module contains a method for pwd command"""

import os


def pwd(*args):
    """Returns current directory"""

    if len(args):
        print("pwd command takes no args")
    else:
        return os.getcwd()
