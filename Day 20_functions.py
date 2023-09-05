def calgmean(a,b):
    gmean = (a*b)/(a+b)
    print(gmean)

def calsum(a,b):
    gmean = (a+b)
    return gmean #like this you can use return function

def greater(a,b):
    if(b<a):
        print(a,"is greater than",b)

    else :
        print(a, "is less than", b)

def islesser(a,b):
    pass #pass function means user will come back later and complete the code but this time ecxute code

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c= calsum(a,b)
calgmean(a,b)
greater(a,b)
print(c)



   
