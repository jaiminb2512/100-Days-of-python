# Round bracket is used to make Tuples
# Tuple can not changble
# Programmer can add any type od data type in Tuple

tup = (1,548,5498,116584,True,"jaimin",54.184)
print(type(tup))

# Positive and negative indexing is same as list
for i in  range (0,len(tup)):
    print(tup[i])

# Checking value in tuple 
if 548 in tup:
    print("YES")