class Shapes():
    def __init__(self, *args):

        for arg in args:
            if type(arg) is int and arg > 0:
                continue
            raise ValueError

    def area(self)->float:
        raise NotImplementedError

    def perimeter(self)->float:
        raise NotImplementedError


