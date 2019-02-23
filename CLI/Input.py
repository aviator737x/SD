"""This module contains entry point"""

from Parser import *
from Analizator import *
import sys


def for_test(line):
        print(line)
        parser = Parser(line)
        analizator = Analizator(parser)
        return analizator.run()


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            parser = Parser(line)
            analizator = Analizator(parser)
            analizator.run()
    except KeyboardInterrupt:
        pass

