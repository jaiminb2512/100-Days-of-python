# dir funtion is use to find which methods in tuple or list 
x = [1, 2, 3]
print(dir(x))
print(x.__class__ ) # This line will show error if the method which written in print function is not in x 

# Dict function give artribution which provided by you in dictionary format
class student:
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch

s1 = student("Jamin","EC")
print(s1.__dict__)

# Help function use to for help
print(help(str))
print(help(student))