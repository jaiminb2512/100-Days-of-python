# A lambda function is a small anonymous functon without a name 

# def double(x):
#     return x*2

double = lambda x: x*2

# Lambda function can take multiple variable
avg = lambda x,y,z : (x+y+z)/3

# Lambda functioin able to contain multiple line 
mul = lambda a,b : print(f"{a} * {b} = {a*b}")

print(double(5))
print(avg(215,54,446))
print(mul(21,2))