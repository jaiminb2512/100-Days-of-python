# Access specifiers or access modifiers in python programming are used to limit the access of class variables and class methods outside of class while implementing the concepts of inheritance.
# Type of Access specifier
""" Public access modifier
    Private access modifier
    Protected access modifier"""
    
# Public access modifier
# All the variables and methods (member functions) in python are by default public. Any instance variable in a class followed by the ‘self’ keyword ie. self.var_name are public accessed.
print("\n")
print("Public access modifier")
class Employee:
    def __init__(self):
       self.name = "Jaimin"
       
e = Employee()
print(e.name)
print("\n") 

# Private access modidier
# Generaly Private access modidier is not accessable 
# But Private access modifier is accessable by using double underscore(__)
print("Private access modidier")
class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"

my_object = MyClass()

print(my_object._nonmangled_attribute) # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute) # Throws an AttributeError
print(my_object._MyClass__mangled_attribute) # Output: I am a mangled attribute
print(e.__dir__())
print("\n")

# Protected access modifier
"""In object-oriented programming (OOP), the term "protected" is used to describe a member (i.e., a method or attribute) of a class that is intended to be accessed only by the class itself and its subclasses. In Python, the convention for indicating that a member is protected is to prefix its name with a single underscore (_). For example, if a class has a method called _my_method, it is indicating that the method should only be accessed by the class itself and its subclasses."""
print("Protected access modifier")
class Student:
    def __init__(self):
        self._name = "Jamin"

    def _funName(self):      # protected method
        return "I am student of Electronics and communication"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
print(dir(obj))
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())
