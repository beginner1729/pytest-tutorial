import math

from src.shapes.base_shape import Shape

class Circle(Shape):

    def __init__(self, radius:float):
        super().__init__(radius)
        self.radius = radius

    def area(self)->float:
        return self.radius * self.radius * math.pi


    def perimeter(self)->float:
        return 2*math.pi*self.radius


