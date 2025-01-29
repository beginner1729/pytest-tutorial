from src.shapes.base_shape import Shape

def difference_area(shape1:Shape, shape2:Shape)->float:
	return abs(shape1.area() - shape2.area())


def difference_perimeter(shape1:Shape, shape2:Shape)->float:
    return abs(shape1.perimeter() - shape2.perimeter())


