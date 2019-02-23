"""This module contains method for wc"""

import os


def wc(count, args):
    """Returns number of lines, words and bytes for a given stream or file"""

    if len(args) != 1:
        print("wc needs 1 file")
    else:
        if count - 1 > 1:
            print("wc needs name of 1 file")
        elif count == 1 and len(args) == 1:
            line = args[0].split("\n")
            lines = len(line)
            words = 0
            for el in line:
                words += len(el.split(" "))
            bytes = len(args[0])
            line = str(lines) + " " + str(words) + " " + str(bytes)
            return line
        elif os.path.isfile(args[0]):
            file = open(args[0])
            lines = 0
            words = 0
            for line in file:
                lines += 1
                words += len(line.split(" "))
            file.close()
            return str(lines) + " " + str(words) + " " + str(os.path.getsize(args[0]))
        else:
            print("No such file")
