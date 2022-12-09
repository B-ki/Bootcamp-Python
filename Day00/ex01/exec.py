import sys

def exec(s):
    str = ""
    for i in s:
        str = i + str
    return str.swapcase()

out = ""
inputArgs = sys.argv
for i in inputArgs[1:]:
    out += ' ' + i

print(exec(out))
