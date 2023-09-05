# By using Enumerate it gives idex with value
# In this be doesn't need to put incerement statement

marks = [12,54,68,87,98,15,65] 

for index,mark in enumerate(marks):
    print(index,mark)
    if (index == 4):
        print("Awesome")
        
    
    
# By default index is start 0 but we can specify different starting value of index
fruits = ['apple', 'banana', 'mango', 'graps'] 
print()
print()

for index,fruit in enumerate(fruits, start = 2):
    print(index,fruit)
    if (index == 4):
        print("Awesome")
        
