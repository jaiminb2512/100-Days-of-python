class shape:
    def __init__(self,x,y):
        self.x  = x
        self.y = y
    
    def area(self):
        return self.x*self.y
    

class circle(shape):
    def __init__(self,radius):
        self.radius = radius   
        super().__init__(radius,radius)
        
    def areaofcircle(self):
        return 3.14 * super().area()



square = shape(5,4)
print(square.area())

circle1 = circle(5)
print(circle1.area())