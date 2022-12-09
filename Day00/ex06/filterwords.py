import sys
import string
import six

if len(sys.argv) != 3:
    print("Takes 2 parameters : 1 string and 1 unsigned int")
    exit()


str = sys.argv[1]
if not isinstance(str, six.string_types):
    print("1st parameter is not a string")
    exit()


try:
    N = int(sys.argv[2])
except ValueError:
    print("2nd parameter is not an int")
    exit()

def countPunctuation(s):
    countPunctuation = 0
    for i in s:
        if i in string.punctuation:
            countPunctuation += 1
    return countPunctuation

newlist = []
for char in string.punctuation:
    sys.argv[1] = sys.argv[1].replace(char, '')
string_list = sys.argv[1].split()
for split in string_list:
    if len(split) > N:
        newlist.append(split)

print(newlist)
        
