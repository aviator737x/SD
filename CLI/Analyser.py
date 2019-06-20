"""This module contains two classes for command analysis"""

from Commands.pwd1 import *
from Commands.exit import *
from Commands.wc import *
from Commands.echo import *
from Commands.cat import *
import subprocess
import shlex

variables = {}
commands = {'pwd': pwd, 'exit': exit, 'wc': wc, 'echo': echo, 'cat': cat}


class Analyser:
    """Form new tree of pipes from 1 parameter: parser
    Field self.structure is dictionary,
    which makes syntax tree structure with pipes in internal vertices and arguments in liefs.
    If the command is assignment, the variable is written in parser.parsed_args.
    Else it is written in syntax tree in order of solving pipes, where the number of command is key in tree."""

    command = ""

    def __init__(self, parsed_args):

        if '=' in parsed_args:
            self.bind(parsed_args[0], parsed_args[2])
            self.key = -1
        else:
            line = parsed_args
            self.structure = {}
            self.key = 0
            key = 0
            self.structure[key] = [0]
            for k in range(len(line)):
                if line[k] != '|':
                    self.make_lief(line[k], key)
                else:
                    key += 1
                    self.key = key
                    self.structure[key] = [0]
                    continue

    def make_lief(self, line, key):
        if line.startswith("\""):
            line = self.find_variables(line)
            element = line[1:]
            words = element.split(" ")
            self.replace_vars(words)
            line = "\""
            for el in words:
                line += el
                line += " "
            line = line[1:len(line) - 1]
            self.structure[key].append(line)
            self.structure[key][0] += 1
        elif line.startswith("\'"):
            self.structure[key].append(line[1:])
            self.structure[key][0] += 1
        elif line.startswith("$") and line:
            if line[1:] in variables:
                line = variables[line[1:]]
            else:
                line = ''
            self.structure[key].append(line)
            self.structure[key][0] += 1
        else:
            line = self.find_variables(line)
            self.structure[key].append(line)
            self.structure[key][0] += 1

    @staticmethod
    def replace_vars(words):
        for i in range(len(words)):
            if words[i].startswith("$") and words[i]:
                if words[i][1:] in variables:
                    words[i] = variables[words[i][1:]]
                else:
                    words[i] = ''

    @staticmethod
    def find_variables(word):
        new_word = ""
        i = 0
        while i < len(word):
            if word[i] == '$':
                i += 1
                var = ""
                while i < len(word) and (word[i] != '$' and word[i] != ' ' and word[i] != '\'' and word[i] != '\"'):
                    var += word[i]
                    i += 1
                new_word += variables[var]
            else:
                new_word += word[i]
                i += 1
        return new_word

    def run(self):
        """Executes command tree"""

        if self.key != -1:
            for i in range(self.key + 1):
                line = self.structure[i]
                if line[1] not in commands:
                    try:
                        args = shlex.split(self.command)
                        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                        result = p.communicate()[0]
                        print(result.decode("utf-8"))
                    except Exception:
                        print("No command", line)
                else:
                    if len(line) > 2:
                        result = commands[line[1]](line[0], line[2:])
                    else:
                        result = commands[line[1]]()
                    if i == self.key:
                        print(result)
                        return result
                    else:
                        self.structure[i+1].append(result)

    @staticmethod
    def bind(var_name, value):
        """Binds name of variable with value"""

        variables[var_name] = value
