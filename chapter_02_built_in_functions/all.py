
def printAll(array):
  if all(array):
    print "All true"
  else:
    print "Not all true"

a = [True, True, True, True]
printAll(a)

b = [True, True, True, False]
printAll(b)

