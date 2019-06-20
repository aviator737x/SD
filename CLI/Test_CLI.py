"""This module contains a set of tests for CLI"""

import unittest
from Commands.pwd1 import *
from Commands.exit import *
from Commands.wc import *
from Commands.echo import *
from Commands.cat import *
import os

class CLITest(unittest.TestCase):
    """The basic class that inherits unittest.TestCase."""

    def test_echo(self):
        assert(echo(1, [""]) == "")
        assert (echo(1, ["abcd"]) == "abcd")
        assert (echo(1, ["aaa", "aaaa"]) is None)
        
    def test_cat(self):
        assert(cat(1, ["abcd"]) == "abcd")
        assert (cat(2, ["test.txt"]) == "abc\nHelloWorld!\n")
        
    def test_pwd1(self):
        assert (pwd() == os.getcwd())


if __name__ == '__main__':
    unittest.main()
