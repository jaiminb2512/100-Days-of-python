#making list
x = [468 , 54846, "Jaimin", True]
print(x)

if "Jaimin" in x:
    print("Yes")

else :
    print("No")

#Making list using for loop and rang function
list1 = [i for i in range(4)]
print(list1)

#we can do airthmatic opration in above example
list2 = [i*i for i in range(4)]
print(list2)

#condition in making list
list3 = [i*i for i in range(10) if i%2==0 ]
print(list3)