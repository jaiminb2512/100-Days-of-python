# String method in python
# By this method programmer can give all the data in one string
# After use of split function all the element is in string type

class student:
    def __init__(self,name,cpi):
        self.name = name
        self.cpi = cpi
        
    def details(self):
        print(f"The name of student is {self.name} and his cpi is {self.cpi}")
        
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
    
s1 = student("jaimin", 9.23)
s1.details()

string = "dev-8.80"
s2 = student.fromstr(string)
s2.details()
