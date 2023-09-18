from For_Dunder import student
from For_Dunder import student2
   
s1 = student()  
print(s1.name)
print(len(s1))

s2 = student2("Dev")
print(s2.name)
print(str(s2)) # This line print str if str is not written or comment at that time this line excute repr method whithout call it 
print(repr(s2)) 

# By this we calling call method 
# If call method is not defined then it gives error
s2() 