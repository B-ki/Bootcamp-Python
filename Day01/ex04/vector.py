import sys


class Vector:
    def __init__(self, *args):
        if len(args) > 2:
            raise ValueError("Need max 2 args, values and shape")
        if not (isinstance(args[0], list)
                or type(args[0])
                or type(args[0] is range)):
            raise TypeError("args[0] must be list of single floats, list of",
                            "list of floats, unsigned int or range of 2 int")
        if type(args[0]) is list:
            if type(args[0][0]) is list:
                for x in args[0]:
                    if not all(isinstance(y, float) for y in x):
                        raise TypeError("List of list of FLOATS required")
            elif type(args[0][0]) is float:
                if not all(isinstance(x, float) for x in args[0]):
                    raise TypeError("List of singles FLOATS required")
            self.values = args[0]
        if type(args[0]) is tuple:
            if args[0][0] > args[0][1]:
                raise ValueError("Must be Start > Stop in range")
            list_arg = [float(x) for x in range(args[0][0], args[0][1])]
            self.values = []
            for i in list_arg:
                sub = []
                sub.append(i)
                self.values.append(sub)
        if type(args[0]) is int:
            if args[0] <= 0:
                raise ValueError("Size must be strictively positive")
            list_arg = [float(x) for x in range(args[0])]
            self.values = []
            for i in list_arg:
                sub = []
                sub.append(i)
                self.values.append(sub)
