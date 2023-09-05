#day 14

age = int(input("Enter your age : "))

if age<18:
    print("You can't vote")

else :
    print("You can vote")

#elif example

x = int(input("Enter the number : "))

if (x%2 == 0 and x%3 == 0):
    print(x,"is divisable by 2 and 3")

elif (x%2 == 0 and x%3 != 0):
    print(x,"is divisable by 2 but not by 3")

elif (x%2 != 0 and x%3 == 0):
    print(x,"is divisable by 3 but not by 2")

else :
    print(x," is neither divisable by 2 nor 3")
