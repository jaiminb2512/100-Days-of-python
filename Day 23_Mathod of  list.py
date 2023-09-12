a = [1,9,54,43,6]
print(a)

# Adding iteams in list
# By use of append function wee can add iteams at last of list
a.append(7)
print(a)

# sort function is used to sort iteams in list
a.sort()
print(a)

# For reverse sorting
a.sort(reverse=True)
print(a)

b = [54,55,46,44,54,64,49,44,58,84,44]
# Getting index of iteam which is in list
# If the two iteams is same at that time index function give index of first occurance
print(b.index(46))

# Programmer use count function to get how many time same iteams is reapeted
print(b.count(44))

# Programmer use copy function formaking copy of list
newlist = b.copy()
print(newlist)

# Putting iteams in particluar index then programmer uses insert function
newlist.insert(1,101)
print(newlist)

c = [58,40,45,54]
# Extend functioin is use to merge two list 
# By using extend function original list is changed
a.extend(c) 
print(a)

# By following  statement programmer making new list which is extend
# list c is joined at the end of newlist and all this stuff is stored in list which name is k
k = newlist + c  
print(k)