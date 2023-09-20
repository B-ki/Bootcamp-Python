import sys

def operations(i, j):
  if not (isinstance(i, int) or isinstance(j, int)):
    print("Error, input must be int")
    return
  print("{: <20}".format("Sum: "), i+j)
  print("{: <20}".format("Difference: "), i-j)
  print("{: <20}".format("Product:"), i*j)
  if (j):
    print("{: <20}".format("Quotient:"), i/j)
    print("{: <20}".format("Remainder:"), i%j)
  else:
    print("ERROR (division by zero)")
    print("ERROR (modulo by zero)")

if (len(sys.argv) != 3):
    print("Usage: python operations.py <number1> <number2>")
    sys.exit()

arg1 = sys.argv[1]
arg2 = sys.argv[2]
flag = True

try:
    arg1_int = int(arg1)
    arg2_int = int(arg2)
except ValueError:
    flag = False

if flag:
    operations(arg1_int, arg2_int) 
else:
    print("AssertionError: only integers")
