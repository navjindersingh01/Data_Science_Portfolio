import pytest
import factorial_logic

factorial = factorial_logic.Factorial()

test_data = [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040),
    (8, 40320),
    (9, 362880)
]

@pytest.mark.parametrize("input,expected",test_data)
def test_factorial_recursion(input,expected):
    assert factorial.factorial_recursion(input) == expected

@pytest.mark.parametrize("input,expected",test_data)
def test_factorial_iterative(input,expected):
    assert factorial.factorial_iterative(input) == expected