# By raise keyword we introduce custom error
a = int(input("Enter the value between 5 and 9 "))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 to 9")
