# Constructor is special method in a class used to create and intialization an object of a class
# constructor is always run when object is created
# Syntax of Constructor
# def  __init __(self):

class Person:
    
    def __init__(self, n, o) :
        print("I am a person")
        self.name = n
        self. occ = o
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = Person("jaimin", "Student")
b = Person("Dev", "HR")
a.info()
b.info()
 