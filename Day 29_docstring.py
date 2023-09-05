def square(n):
    #this is doc string not comment  
    #doc string always write in triple cotation and it below the function name and above the function body
    """This function takes integer n and returns it's square"""
    print(n**2)
    
    
x = int(input("Enter a number of which you want find square : "))
square(x)

#Like this you can print doc string in your code
print(square.__doc__)