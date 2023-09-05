#printing table of any given number

x = int(input("Enter the number which you want to print table : "))
i = 1

print("Table in forward :")
while(i<=10):
    print(x, "*",i,"=",x*i)
    i = i+1

print("Table in reverse :")
i=10
while(i>0):
    print(x, "*",i,"=",x*i)
    i = i-1

#we can use else with while loop
#when condition is false then else will excute

else:
    print("I am inside the else")

print("Table printed using do while loop")