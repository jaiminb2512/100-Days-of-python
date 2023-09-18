# Super keyword is use to call parent class when you are in child class
# By use of super programmer can call constructor 

class parentclass:
    def __init__(self,name):
        self.name = name
    
    def parent_method(self):
        print("This is parent class 1")
        
class childclass(parentclass):
    def __init__(self,name,id):
        super().__init__(name)
        self.id = id
    
    def parent_method(self):
        # print("jaimin")
        super().parent_method()
    
    def child_method(self):
        print("This is child method")
        
object1 = childclass("Dev","445")
object1.child_method()
object1.parent_method()
print(object1.id)
print(object1.name)