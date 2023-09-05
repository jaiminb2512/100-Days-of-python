ep1 = {122 : 56, 245 : 89, 184 : 60}
ep2 = {540 : 90, 498 : 71}
ep3 = {546 : 54, 548 : 63, 656 : 10, 648 : 61}

#Merge two dictionary
ep1.update(ep2)
print(ep1)

#To eliminate one pair of key and value
ep3.pop(546)
print(ep3)

#To remove last pair of key and value
ep3.popitem()



#To clear dictionary
ep1.clear()
print(ep1)

#if you want to delete only one pair of key and value 
del ep3[656]
print(ep3)

#To delete whole dictionary
del ep1
