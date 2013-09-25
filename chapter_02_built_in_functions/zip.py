a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [5, 6, 7, 8, 9]
d = range(0, 20)
slice_size = 3

#print zip(a, b)
#print zip(c, a)

print d
print zip(*(iter(d),) * slice_size)
