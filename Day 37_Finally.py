# Finally is always run whether the function is returned or not
def func1():
    try:
        l=[1,5,9,4,7]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0
        
    finally:
        print("I am always excuted")       
        
x = func1()
print(x)