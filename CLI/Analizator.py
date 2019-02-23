"""This module contains two classes for command analysis"""

from pwd1 import *
from exit import *
from wc import *
from echo import *
from cat import *

variables = {}
commands = {'pwd': pwd, 'exit': exit, 'wc': wc, 'echo': echo, 'cat': cat}


class Tree:
    """Contains tree of commands"""

    tree = {}


class Analizator:
    """Form new tree of pipes from 1 parameter: parser"""

    def __init__(self, parser):
        """Inits Analizator with 1 parameter:
        :param parser: type of Parser"""

        if '=' in parser.parsed_args:
            self.bind(parser.parsed_args[0], parser.parsed_args[2])
            self.key = -1
        else:
            line = parser.parsed_args
            self.structure = Tree()
            flag = True
            self.key = 0
            key = 0
            self.structure.tree[key] = [0]
            for k in range(len(line)):
                if flag and line[k] != '|':
                    if line[k].startswith("\""):
                        element = line[k][1:]
                        words = element.split(" ")
                        for i in range(len(words)):
                            if words[i].startswith("$") and words[i]:
                                if words[i][1:] in variables:
                                    words[i] = variables[words[i][1:]]
                                else:
                                    words[i] = ''
                        line[k] = "\""
                        for el in words:
                            line[k] += el
                            line[k] += " "
                        line[k] = line[k][1:len(line[k])-1]
                        self.structure.tree[key].append(line[k])
                        self.structure.tree[key][0] += 1
                    elif line[k].startswith("\'"):
                        self.structure.tree[key].append(line[k][1:])
                        self.structure.tree[key][0] += 1
                    elif line[k].startswith("$") and line[k]:
                        if line[k][1:] in variables:
                            line[k] = variables[line[k][1:]]
                        else:
                            line[k] = ''
                        self.structure.tree[key].append(line[k])
                        self.structure.tree[key][0] += 1
                    else:
                        self.structure.tree[key].append(line[k])
                        self.structure.tree[key][0] += 1
                else:
                    key += 1
                    self.key = key
                    self.structure.tree[key] = [0]
                    continue

    def run(self):
        """Executes command tree"""

        if self.key != -1:
            for i in range(self.key + 1):
                line = self.structure.tree[i]
                if line[1] not in commands:
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
                        self.structure.tree[i+1].append(result)

    @staticmethod
    def bind(var_name, value):
        """Binds name of variable with value"""

        variables[var_name] = value
