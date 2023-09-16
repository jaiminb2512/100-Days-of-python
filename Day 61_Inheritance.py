# Inharitance
# Inharitance is useful to in predifined class
# Inharitance accept class and then it will change it4
"""When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance."""

class emplyee:
    def __init__(self,name, id) :
        self.name  = name
        self.id = id
        
    def showdetails(self):
        print(f"The name of the employees is {self.name} and the id is {self.id}")
        
class Programmer(emplyee):
    def showlanguage(self):
        print("The default language is Python")
        
e1 = emplyee("Jaimin", 400)
e1.showdetails()

e2 = Programmer("Harry", 300)
e2.showdetails()
e2.showlanguage()

