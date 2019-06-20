"""This module contains a class for command line parsing.
It takes a string received from terminal and creates field self.parsed_args that is a list,
containing separated tokens of command."""


class Parser:
    def __init__(self, line):
        if line:
            line = line[:len(line) - 1]
        self.parsed_args = []
        self.line = line

    @staticmethod
    def starts_with_quote(s):
        return s.startswith("\"") or s.startswith("\'")

    @staticmethod
    def contains_no_space(s):
        return len(s.split(" ")) == 1

    def parse(self, line = None):
        if line is None:
            line = self.line
        if not self.starts_with_quote(line) \
                and self.contains_no_space(line) and line.find("=") != -1:
            self.parsed_args = [line.split("=")[0], '=', line.split("=")[1]]
            return
        if line.startswith("\""):
            ind = 0
            for i in range(1,len(line)):
                if line[i] == '\"' and line[i-1] != '\\':
                    ind = i
                    break
            self.parsed_args.append(line[0:ind])
            ind += 1
            line = line[ind:]
            while line and line.startswith(' '):
                line = line[1:]
            if line:
                self.parse(line)
        elif line.startswith("\'"):
            ind = 0
            for i in range(1,len(line)):
                if line[i] == '\'' and line[i-1] != '\\':
                    ind = i
                    break
            self.parsed_args.append(line[0:ind])
            ind += 1
            line = line[ind:]
            while line and line.startswith(' '):
                line = line[1:]
            if line:
                self.parse(line)
        elif line.startswith('|'):
            self.parsed_args.append('|')
            line = line[2:]
            self.parse(line)
        else:
            s = line.split(" ")[0]
            self.parsed_args.append(s)
            line = line[len(s):]
            if line:
                line = line[1:]
                self.parse(line)

    def reinit(self, line):
        if line:
            line = line[:len(line) - 1]
        self.line = line
        self.parsed_args = []


