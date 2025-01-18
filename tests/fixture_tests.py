import pytest
from src.shapes.circle import Circle
from src.shapes.rectangle import Rectangle
from src.utils.utils import *

# Define a fixture
@pytest.fixture
def circle_fixture():
    return Circle(10)

@pytest.fixture
def rectangle_fixture():
    return Rectangle(10, 10)

def test_area_difference(circle_fixture):
    difference = difference_area(
        circle_fixture, circle_fixture
    )
    assert difference == 0

def test_perimeter_difference(rectangle_fixture):
    difference = difference_perimeter(
        rectangle_fixture, rectangle_fixture
    )

    assert difference == 0
