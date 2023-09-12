# is and == are comparision operator
a = 4
b = "4"

print(a is b) # checking the exact location of object in memory
print(a == b) # value

c = [1,2,3]
d = [1,2,3]
print(c is d) # Output is false
print(c == d) # Output is true

# when we made constant value or same string or immutable data type than ans of is ans == operator is  true
e = 3
f = 3
print( e is f)
print( e == f)