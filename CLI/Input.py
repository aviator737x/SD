"""This module contains entry point"""

from Parser import *
from Analyser import *
import sys

if __name__ == '__main__':
    while True:
        try:
            parser = Parser("")
            for line in sys.stdin:
                if line == '\n':
                    continue
                parser.reinit(line)
                parser.parse()
                analyser = Analyser(parser.parsed_args)
                analyser.command = line
                analyser.run()
        except ExitException:
            break
        except Exception:
            print("Command could not be recognized. Please, try again.")

