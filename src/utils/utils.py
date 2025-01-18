from src.shapes.base_shape import Shapes

def difference_area(shape1:Shapes, shape2:Shapes)->float:
	return abs(shape1.area() - shape2.area())


def difference_perimeter(shape1:Shapes, shape2:Shapes)->float:
    return abs(shape1.perimeter() - shape2.perimeter())


