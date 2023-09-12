# If you want to change tuple first change tuple into list than chage that list after this convert that list in to  tuple
tup = (1,548,5498,116584,True,"jaimin",54.184)
newlist = list(tup)
newlist.insert(1,101)
tup =  tuple(newlist)
print(tup)

tuple1 = (0,1,2,3,3,4,3,5,6,7,8,9,10)
res = tuple1.count(3)
print('Count of 3 in tuple1 is :',res)

res2 = tuple1.index(4)
print('Index of 3 in tuple1 is :',res2)

# Finding the index of value in range 
# (3,2,9) means finding idex 3 in range of 2 to 9
res3 = tuple1.index(3,2,9)
print('Index of 3 in range of 2 to 9 tuple1 is :',res3)