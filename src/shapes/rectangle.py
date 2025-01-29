from src.shapes.base_shape import Shape

class Rectangle(Shape):

    def __init__(self, length:float, breadth:float):
        super().__init__(length, breadth)
        self.length = length
        self.breadth = breadth

    def area(self)->float:
        return self.length * self.breadth

    def perimeter(self)->float:
        return (self.length + self.breadth) * 2


