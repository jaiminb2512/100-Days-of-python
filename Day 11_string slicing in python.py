names = "jaimin, dhruvil, darshan, vishal"

# Using length function programmer getting the len of variable
print(len(names))

# Writing following statement program can sclice the variable
print(names[0:6])

# When the index in not given python taking 0 to length of variable
print(names[:])

# If program doesn't wrote index in right side python take index 0
print(names[:21])

# If program doesn't wrote index in left side python take lenght of variable
print(names[6:])

# The nagative index strat from right side of variable
print(names[12:-1]) #This and following statement is sames
print(names[12:len(names)-1])

