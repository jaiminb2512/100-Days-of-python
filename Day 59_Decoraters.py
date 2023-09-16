# Decoraters are accept function and return the function which is modified
# you can use decoraters at the stating of that function like thes

# @decorater function name
# def hello():
#     print("HELLO JAIMIN")

# hello()

# or 

# def hello():
#     print("HELLO JAIMIN")

# decorator function name(hello)() 

def greet(fx):
    def mfx():
        print("Good  morning")
        fx()
        print("Thanks for using")
    return mfx
        
# @greet
def hello():
    print("HELLO JAIMIN")
    
def sum (a,b):
    print(a+b)
    
greet(hello)()