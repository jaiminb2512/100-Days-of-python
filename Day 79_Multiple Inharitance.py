# Multiple inhritance
# In multiple inharitance one child class which have multiple parent class

class student:
    def __init__(self,name):
        self.name = name
    
    def show(self):
        print(f"Name of student is {self.name}")    
    
class branch:
    def __init__(self,branch):
        self.branch = branch
        
    def show(self):
        print(f"Name of branch of student is  {self.brach}")   
        
class studentbranch(student,branch):
   def __init__(self,name, branch):
        self.name = name
        self.branch = branch

s1 = studentbranch("jaimin", "EC")
print(s1.name)
print(s1.branch)
s1.show() #This will the first parent class of the child class 
          #It will change when we change the order of the parent class's order
          
print(studentbranch.mro()) # This show where the function will find first 
                           # It will change when we change the order of the parent class's order 