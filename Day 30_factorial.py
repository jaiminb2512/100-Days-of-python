def factorial(x):
    if (x == 0 or x== 1) :
            return 1 
    else :
      
     return x*factorial(x-1)

n = int(input("Enter the value of number : "))
print("Factorial of ", n, "is",factorial(n) )