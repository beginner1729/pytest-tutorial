from src.shapes.base_shape import Shapes

class Rectangle(Shapes):

    def __init__(self, length:float, breadth:float):
        self.length = length
        self.breadth = breadth

    def area(self)->float:
        return self.length * self.breadth

    def perimeter(self)->float:
        return (self.length + self.breadth) * 2


