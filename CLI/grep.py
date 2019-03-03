"""This module contains a method for grep"""

import argparse
import re


def grep(count, args):
    """Returns strings that contain pattern. Uses keys:
    -i: ignore case
    -w: search words entirely
    -A n: returns string corresponding to pattern and n strings after it, if they exist
    pattern: is python regexp, must be given as penultimate argument
    name:  is name of file or stream received from pipe, must be ultimate parameter
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', action='store_true', help='Makes grep insensitive to case')
    parser.add_argument('-w', action='store_true', help='Searches only words entirely')
    parser.add_argument('-A', action='store', type=int, help='Prints n strings after string with coincidence', default=0)
    parser.add_argument('pattern', action='store', help='String to be found')
    parser.add_argument('name', action='store', help='Applies grep to name')
    arguments = parser.parse_args(args)
    stream = arguments.name.split("\n")
    if count == len(args) + 1:
        stream = []
        file = open(arguments.name)
        for line in file:
            stream.append(line)
    if arguments.w:
        arguments.pattern = "\\b" + arguments.pattern + "\\b"
    indices = []
    for i in range(len(stream)):
        if arguments.i and re.search(arguments.pattern, stream[i], re.IGNORECASE) is not None:
            indices.append(i)
        elif re.search(arguments.pattern, stream[i]) is not None:
            indices.append(i)
    result = ""
    for ind in indices:
        result = result + stream[ind]
        for i in range(1, arguments.A + 1):
            if ind + i in indices:
                break
            if ind + i < len(stream):
                result = result + stream[ind + i]
        if arguments.A != 0 and result.endswith("\n"):
            result = result + "-----\n"
    return result
