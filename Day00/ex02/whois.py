import sys

def whois(i):
  if not (isinstance(i, int)):
    print("Error, input must be int")
  else:
    if (i%2):
     print("I'm Odd")
    elif not i:
     print("I'm Zero")
    else:
     print("I'm Even")

if (len(sys.argv) != 2):
    print("Provide 1 and only 1 argument please")
    exit

arg1 = sys.argv[1]

flag = True

try:
    arg1_int = int(arg1)
except ValueError:
    flag = False

if flag:
    whois(int(arg1))
else:
    print("The input is not an integer")
