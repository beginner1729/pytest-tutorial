import pytest
import math

from src.shapes.circle import Circle
from src.shapes.rectangle import Rectangle
from src.utils.utils import *

def test_difference_area():

    circle1 = Circle(10)
    circle2 = Circle(20)

    assert difference_area(
        circle1, circle2
    ) == math.pi*300


def test_value_error_circle():
    with pytest.raises(ValueError):
        Circle(-2)

def test_value_error_rectangle():
    with pytest.raises(ValueError):
        Rectangle(10,0)

