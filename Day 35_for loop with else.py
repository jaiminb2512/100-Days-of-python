# We can use else statement with for and while loop
# when i is not statisfy the loop's condition the else is excute
for i in range(6):
    print(i)

else:
    print()

# In this example else is not excute because if condition is satisfied
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print()
    
