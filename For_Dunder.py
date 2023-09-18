class student:
    name = "jaimin"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
 
 
class student2: 
    def __init__(self,name):
        self.name =  name
        
    def __str__(self):
        return f"The name of the studet is {self.name} str"
    
    def __repr__(self):
        return f"The name of the studet is {self.name} repr"
    
    def __call__(self):
        print(f"I am student of EC")