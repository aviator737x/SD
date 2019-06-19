"""This module contains entry point"""

from Parser import *
from Analizer import *
import sys


def for_test(line):
        print(line)
        parser = Parser(line)
        analizer = Analizer(parser)
        return analizer.run()


if __name__ == '__main__':
    try:
        parser = Parser("")
        for line in sys.stdin:
            parser.reinit(line)
            parser.parse()
            analizer = Analizer(parser.parsed_args)
            analizer.run()
    except ExitException:
        pass

