a = {1, 23, 4, 9}
b = {1, 5, 4, 7, 8}

print(type(a))
print(type(b))

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#changing the sets
c = a.difference(b) 
print(c)
