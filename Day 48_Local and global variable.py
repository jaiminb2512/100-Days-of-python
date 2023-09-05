# Global variable is defined in program 
# Local variable defined in function of the program 
# local variable is destroyed after excution of function but global variable not 
# name of local and global variable is same than it will be over writed in that function

x = 4

def hello():
    x = 5
    print(f"The value of local variable x is {x}")
    
print(f"The value of global variable x is {x}")
hello()
print(f"The value of local variable x is {x}")



# global keyword
y = 40
print()
print()
print("Use of global keyword")
print(f"The value of y is {y} befor function call")

def hello():
    global y
    y = 50
    
hello()
print(f"The value of y is {y} after function call")

    
