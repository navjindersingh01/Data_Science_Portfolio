import pytest
import Method_iterative as mi

test_data = [
                (3,[0,1,1]),
                (4,[0,1,1,2]),
                (5,[0,1,1,2,3])
            ]

@pytest.mark.parametrize("input,expected",test_data)
def test_fibonacci_iterative(input,expected):
    assert mi.fibonacci_iterative(input) == expected

@pytest.mark.parametrize("input,expected",test_data)
def test_fibonacci_optimized(input,expected):
    assert mi.fibonacci_optimized(input) == expected

@pytest.mark.parametrize("input,expected",test_data)
def test_fibonnaci_recursive(input,expected):
    fib = []
    for i in range(input):
        fib.append(mi.fibonacci_recursive(i))

    assert fib == expected

@pytest.mark.parametrize("input,expected",
                         [
                             ([0,1,1],2),
                             ([0,1,1,2],4),
                             ([0,1,1,2,3],7)
                         ])
def test_fibonacci_sum(input,expected):
    assert mi.fibonacci_sum(input) == expected

@pytest.mark.parametrize("input,expected",[
    (3,[1,1,1]),
    (4,[1,1,1,1]),
    (8,[1,1,1,1,1,1,1,2])
])
def test_fibonacci_size(input,expected):
    assert mi.fibonacci_size(input) == expected
    