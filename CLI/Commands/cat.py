"""This module contains method for cat"""

import os


def cat(count = 0, args = ""):
    """Returns stream of strings from file or entry stream"""

    if count == 0:
        while True:
            s = input()
            if s == "exit":
                return ""
            print(s)
    elif count > 2:
        print("cat needs 1 file")
    elif len(args) == 1 and count == 1:
        return args[0]
    else:
        if os.path.isfile(args[0]):
            result = ""
            file = open(args[0])
            lines = file.readlines()
            for i in range(len(lines)):
                result += lines[i]
            file.close()
            return result
        else:
            return args[0]
