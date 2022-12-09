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
