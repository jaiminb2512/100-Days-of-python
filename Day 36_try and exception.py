a = input("Enter the number : ")
print("Multiplication table is  :")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
    
except Exception as e:
    print(e)    
    
# we can use except like this too 
# except: 
#   print("Error occured")
    
print("End of the code")
