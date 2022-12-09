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
