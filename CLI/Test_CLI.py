"""This module contains a set of tests for CLI"""

import unittest
from Input import *


class CLITest(unittest.TestCase):
    """The basic class that inherits unittest.TestCase. It contains
    the main tests for module "Input.py" """

    def test_echo_with_out_quoting(self):
        """check that echo prints a given string with out quoting"""
        self.assertEqual(for_test("echo 123\n"), "123")

    def test_echo_with_full_quoting(self):
        """check that echo prints a given string with full quoting"""
        self.assertEqual(for_test("echo \"123\"\n"), "123")

    def test_echo_with_weak_quoting(self):
        """check that echo prints a given string with weak quoting"""
        self.assertEqual(for_test("echo \'123\'\n"), "123")

    def test_echo_with_dollar_with_out_qouting(self):
        """check that echo prints a given string with out quoting with $variable"""
        for_test("x=123\n")
        self.assertEqual(for_test("echo $x\n"), "123")

    def test_echo_with_dollar_with_full_qouting(self):
        """check that echo prints a given string with full quoting with $variable"""
        for_test("x=123\n")
        self.assertEqual(for_test("echo \"$x\"\n"), "123")

    def test_echo_with_dollar_with_weak_qouting(self):
        """check that echo prints a given string with weak quoting with $variable"""
        for_test("x=123\n")
        self.assertEqual(for_test("echo \'$x\'\n"), "$x")

    def test_wc_on_file(self):
        """check that wc works on file test.txt"""
        self.assertEqual(for_test("wc test.txt\n"), "2 2 15")

    def test_cat_on_file(self):
        """check that cat works on file test.txt"""
        self.assertEqual(for_test("cat test.txt\n"), "abc\nHelloWorld!")

    def test_pipe_from_echo_to_cat(self):
        """check that pipe translates stream from echo to cat"""
        self.assertEqual(for_test("echo 123 | cat\n"), "123")

    def test_pipe_from_echo_to_wc(self):
        """check that pipe translates stream from echo to wc"""
        self.assertEqual(for_test("echo 123 | wc\n"), "1 1 3")

    def test_pipe_from_cat_to_wc(self):
        """check that pipe translates stream from cat to wc"""
        self.assertEqual(for_test("cat test.txt | wc\n"), "2 2 15")

    def test_complex_pipe(self):
        """tests complex command"""
        for_test("x=2\n")
        self.assertEqual(for_test("echo \"123 $x\"  | cat | wc | cat\n"), "1 2 5")

    def test_pwd(self):
        """tests pwd command"""
        self.assertEqual(for_test("pwd\n")[-3:], "CLI")

    def test_grep_for_stream(self):
        """tests grep command for stream"""
        self.assertEqual(for_test("echo \"aaaa\" | grep a\n"), "aaaa")

    def test_grep_for_file_with_out_keys(self):
        """tests grep command for file with out keys"""
        self.assertEqual(for_test("grep abc test.txt\n"), "abc\n")

    def test_grep_for_key_i(self):
        """tests grep command for key -i"""
        self.assertEqual(for_test("echo \"aaaa\" | grep -i A\n"), "aaaa")

    def test_grep_for_key_w(self):
        """tests grep command for key -w"""
        self.assertEqual(for_test("echo \"aaaa abcs\" | grep -w aaa\n"), "")

    def test_grep_for_key_A(self):
        """tests grep command for key -A"""
        self.assertEqual(for_test("grep -A 1 abc test.txt\n"), "abc\nHelloWorld!")


if __name__ == '__main__':
    unittest.main()