def printAny(array):
  if any(array):
    print "Atleast one true"
  else:
    print "None are true"

a = [False, False, False, False]
printAny(a)

b = [False, False, True, False]
printAny(b)

