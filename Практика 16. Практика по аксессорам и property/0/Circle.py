from math import pi
class Circle:
    def __init__(self, radius):
        self._radius = radius
        self._diametr = 2*radius
        self._area = pi * radius **2

    def get_radius(self):
        return self._radius
    
    def get_diametr(self):
        return self._diametr
    
    def get_area(self):
        return self._area
    
circle = Circle(1) 
print(circle.get_radius()) 
print(circle.get_diametr()) 
print(round(circle.get_area())) 

circle = Circle(5) 
 
print(circle.get_radius()) 
print(circle.get_diametr()) 
print(round(circle.get_area()))