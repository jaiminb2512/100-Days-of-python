# Static method
# Static method is function which performs mathamatic opration in class
# It always decorated by @staticmethod
# It is accesable directly and it is does not required self declaration
# Programmer can access it by using class name
# Static method is useful when you want send any type of mathamatical oparation with class

class math:
    def __init__(self,num):
        self.num = num
        
    def subtonum(self,n):
        self.num = self.num - n
        
    @staticmethod 
    def sub(a, b):
        return a - b
    
a = math(7)
print(a.num)
a.subtonum(2)
print(a.num)

print(a.sub(5,6))
print(math.sub(84,64))