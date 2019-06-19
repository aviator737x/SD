"""This module contains entry point"""

from Parser import *
from Analyser import *
import sys

if __name__ == '__main__':
    try:
        parser = Parser("")
        for line in sys.stdin:
            parser.reinit(line)
            parser.parse()
            analyser = Analyser(parser.parsed_args)
            analyser.run()
    except ExitException:
        pass

