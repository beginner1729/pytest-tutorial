import pytest
import math
import json

from unittest.mock import patch
from src.shapes.rectangle import Rectangle
from src.shapes.circle import Circle
from src.api.get_data import request_data, process_data_to_objs


class TestShapes():

    def setup_method(self):
        self.circle = Circle(10)
        self.rectangle = Rectangle(10, 20)

    def teardown_method(self):
        del(self.rectangle)
        del(self.circle)

    def test_area(self):
        assert self.rectangle.area() == 200 \
                and self.circle.area() == math.pi*100

    def test_perimenter(self):
        assert self.rectangle.perimeter() == 60 \
                and self.circle.perimeter() == math.pi*20

    @patch('requests.get')
    def test_request(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = json.dumps({
            'shapeTypes' : [{
                'type':'circle',
                'params': [10]
            }]
        })

        request_json = request_data('testurl')
        print(type(request_json))
        shape_objs = process_data_to_objs(
            request_json)

        assert len(shape_objs) == 1 and \
                shape_objs[0].area() == self.circle.area()


    def test_compute(self):
        pass

    @pytest.mark.xfail(reason="This feature is not implemented yet")
    def test_fail(self):
        assert self.circle.dimension == 2

