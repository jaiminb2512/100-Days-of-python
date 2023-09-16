# Class variable
# When any variable is declared in class then it called class variable

# Instance variable
# Instance variable change only data of that object in which it is declared

class student:
    collegename = "L.D. college of engineerig" # Class variable
    def __init__(self,name,branch):
        self.name = name
        self.branch = branch
        
    def details(self):
        print(f"The name of the student is {self.name} and branch of him is {self.branch}. He study in {self.collegename}")
        
s1 = student("Jaimin", "EC")
s1.collegename = "VGEC" # Instance variable
s1.details()       

s2 = student("Dhruvil", "IT")
s2.details()

# By following code 
student.collegename = "Nirma University"

s3 = student("Darshan", "Computer")
s3.details()