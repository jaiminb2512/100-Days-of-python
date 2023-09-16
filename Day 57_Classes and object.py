# Classes
# A class is a blueprint or a templete for creating objects, providing initial values for state, and implementions of behavior.
# The user-defined objects are created using keyword.
class Person:
    name = "Jaimin"
    occupation = "Student"
    age = "19"
    
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
b = Person()
a.name = "Vishal"
a.occupation = "Civil engineer"
a.age = 22

print(a.name)
print(a.occupation)
print(a.age)


b.name = "Dev"
b.occupation = "accountant"

a.info()
b.info()
