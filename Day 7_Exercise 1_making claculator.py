# Making calculator which performs multiplicaton, Additon, Subtracton, 

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
print("Enter 1 for Addition")
print("Enter 2 for Sunstracion")
print("Enter 3 for Division")
print("Enter 4 for Multiplication")
print("Enter 5 for Exponetional")
print("Enter 6 for Floor Division")
o = int(input("Enter your choics 1 to 6 : "))
    
if (o == 1):
    print(f"The Addition of {a} + {b} is {a+b}")
elif (o == 2):
    print(f"The Sunstracion of {a} - {b} is {a-b}")
elif (o == 3):
    print(f"The Division of {a} / {b} is {a/b}")
elif (o == 4):
    print(f"The Multiolication of {a} * {b} is {a+b}")
elif (o == 5):
    print(f"The Exponetional of {a} ^ {b} is {a**b}")
elif (o == 6):
    print(f"The Floor Division of {a} // {b} is {a//b}")
else :
    print("invalid input")
