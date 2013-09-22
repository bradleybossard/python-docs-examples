
try:
    set
except NameError:
    from sets import Set as set

s = set([1, 2, 3, 4, 5])
t = set([4, 5, 6, 9, 11, 'boots'])

s.add(6);
print s

s.pop();
print s

s.discard(4);
print s

print 't = ' + str(t)

print 'intersection = ' + str(s.intersection(t))

