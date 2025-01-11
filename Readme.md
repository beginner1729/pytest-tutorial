# Pytest

Here we learn about pytest a python repo for creating test cases


## Introduction

```
def my_fucntion(a, b):
	return a/b
```




To write the test case of the following we use the pytest

```

def test_divide():
	assert 2.0 == my_function(10, 5)
```

We can even test for exceptions
```
def test_divide_zero_test():
	with pytest.raises(ZeroDivisionError):
		myfucntion(10, 0)
```

To run all the test cases we need to enter the following command

`pytest path/to/test_File.py`

For our use case lets assume we have the following classes

```
import math

class Shapes():
    def __init__(self):
        pass

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

class Rectange(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return (self.length + self.breadth) * 2


class Circle(Shape):
    
    def __init__(self, radius):
       self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi


    def perimeter(self):
        return 2*math.pi*self.radius

```


## Fixtures

Fixtures are a way in which we can have only one decleration of the
method/object string ints or any other value and use those decleration in our
tests. 

```
import pytest

# Define a fixture
@pytest.fixture
def my_fixture():
  return "Hello, world!"

# Test function using the fixture
def test_my_function(my_fixture):
  # Access the value returned by the fixture
  greeting = my_fixture
  assert greeting == "Hello, world!"

```

Returning back to our `Shapes` example we can see that we can have a single
decleration for our shapes and can use them in our test cases

```
import pytest
from shapes import *
import math

#define a rectangle fixture
@pytest.fixture
def my_rectangle():
    return Rectange(10,5)

@pytest.fixture
def my_circle():
    return Circle(10)

def test_circle_area(my_circle):
    assert my_circle.area() == math.pi * 100

def test_rectangle_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == 30


```
For ease we should put the fixtures in a configuration file and we can access
those files during our test

## Mark

For convinence pytest allows multiple mark functionalities where we can mark a
a test to be slow or to be skipped during testing.

Some exmaples for skip are as follows

### Skip

```
import pytest
import sys

@pytest.mark.skipif(
        sys.version_info < (3, 8), reason="Requires Python 3.8 or higher")
def test_my_function():
    # Test code that will be skipped on older Python versions
    assert True


@pytest.mark.skip(reason="This test is not implemented yet")
def test_my_function():
    # Test code that will be skipped
    assert True

```
Example for slow are
```

### Marking Slow

import pytest
import time

@pytest.mark.slow
def test_my_slow_function():
    time.sleep(5)  # Simulate a slow operation
    assert True
```
Now marking slow helps to run us those test cases that are not slow

`pytest -m "not slow"`
`pytest -m "slow"`


### Xfail

`pytest.mark.xfail`
This decorator allows you to mark tests that are expected to fail.
Some examples are as follows


```

import pytest
import sys

@pytest.mark.xfail(reason="This feature is not implemented yet")
def test_my_function():
  # Test code that is expected to fail
  assert False


@pytest.mark.xfail(sys.version_info < (3, 8), reason="Known issue on older Python versions")
def test_my_function():
  # Test code that is expected to fail on older Python versions
  if sys.version_info < (3, 8):
      assert False
  else:
      assert True
```
One can use strict=True in the decorator to report failure if the test
unexpectedly passes

```
import pytest

@pytest.mark.xfail(reason="This test should fail", strict=True)
def test_my_function():
  # Test code that is expected to fail
  assert False

```



## Mock Functionality

Mock helps with mocking the functionality of the 3rd party codes or calls to
dbs without having to make the actual call. and mocking the call with some
dummy value

```
import unittest
from unittest.mock import patch
import requests

def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    response.raise_for_status()  # Raise an exception for bad status codes
    return response.json()

class TestGetUserData(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_data_success(self, mock_get):
        # Configure the mock to return a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'id': 1, 'name': 'Alice'}

        # Call the function
        user_data = get_user_data(1)

        # Assert the expected result
        self.assertEqual(user_data, {'id': 1, 'name': 'Alice'})


```

in this we see we have overridden the functionaly of requests.get

