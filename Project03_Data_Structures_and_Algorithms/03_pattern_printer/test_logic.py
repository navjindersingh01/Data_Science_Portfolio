import pytest
import logic

input = 5
pattern = logic.Patterns(input)

pyramid_data = [("""    *
   ***
  *****
 *******
*********""")]

inverse_pyramid_data = [("""*********
 *******
  *****
   ***
    *""")]

right_triangle_data = [("""*
**
***
****
*****""")]

inverse_right_triangle_data = [("""*****
****
***
**
*""")]

diamond_data = [("""    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *""")]

@pytest.mark.parametrize("expected",pyramid_data)
def test_pyramid(expected):
    assert pattern.pyramid() == expected

@pytest.mark.parametrize("expected",inverse_pyramid_data)
def test_inverse_pyramid(expected):
    assert pattern.inverse_pyramid() == expected

@pytest.mark.parametrize("expected",right_triangle_data)
def test_right_triangle(expected):
    assert pattern.right_triangle() == expected

@pytest.mark.parametrize("expected",inverse_right_triangle_data)
def test_inverse_right_triangle(expected):
    assert pattern.inverse_right_triangle() == expected

@pytest.mark.parametrize("expected",diamond_data)
def test_diamond(expected):
    assert pattern.diamond() == expected