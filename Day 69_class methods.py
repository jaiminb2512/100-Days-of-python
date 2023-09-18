# Classmethods
# Classmethod is use to change class 
# It accept class in place of self
# It use as a decorator

class student:
    nameofclg = "silver oak"
    def student(self,name):
        self.name = name 
    
    def details(self):
        print(f"The name of student is {self.name} and name of college is {self.nameofclg}")
    
    @classmethod
    def newclg(cls,newclg):
        cls.nameofclg = newclg 
        
s1 = student()
s1.name = "jaimin"
s1.details()
s1.newclg("L.D. college of engineering")
s1.details()