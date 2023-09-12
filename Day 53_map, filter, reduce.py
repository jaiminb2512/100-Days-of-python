# Map function applies to function to each element in a sequence and returns a new sequence containing  the transfered iteams
# Programmer must typecasting map function
# Syntax of map function is
# map(function,iterable)

cube = lambda x: x*x*x

l = [1,2,3,4,5,6]
# newl = []
# for  i in l:
#     newl.append(cube(i))

newl1 = list(map(cube,l))    
print(newl1)

# Syntax of filter function is
# filter(function,iterable)
# Filter function filter the values by given condition
filter_function = lambda a : a>2
newl2 = list(filter(filter_function,l))
print(newl2)

# Programmer can direct use lambda function in place of function
newl3 = list(map(lambda x: x*x,l))    
print(newl3)

# Reduce function applies the functionto the first two elements in the iterable and then applies the function to the result and the next element, ans so on.
from functools import reduce
sum = reduce(lambda x,y : x+y, l)
print(sum)