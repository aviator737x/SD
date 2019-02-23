"""This module contains a class for command line parsing"""

class Parser:
    def __init__(self, line):
        """Inits Parser with 1 parameter
        :param line: string received from shell"""

        if line:
            line = line[:len(line) - 1]
        self.parsed_args = []
        self.parse(line)

    def parse(self, line):
        """Parses string with 1 parameter:
        :param line: received string"""

        if not line.startswith("\"") and not line.startswith("\'") \
                and len(line.split(" ")) == 1 and line.find("=") != -1:
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


