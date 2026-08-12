import pytest
from reorder_list import reorder_list, build, to_list


def reordered(values):
    h = build(values)
    reorder_list(h)
    return to_list(h)


def test_even_length():
    assert reordered([1,2,3,4]) == [1,4,2,3]

def test_odd_length():
    assert reordered([1,2,3,4,5]) == [1,5,2,4,3]

def test_two_elements():
    assert reordered([1,2]) == [1,2]

def test_single_element():
    assert reordered([1]) == [1]

def test_empty():
    reorder_list(None)   # should not raise

def test_three_elements():
    assert reordered([1,2,3]) == [1,3,2]

def test_all_same_values():
    assert reordered([5,5,5,5]) == [5,5,5,5]

def test_length_preserved():
    original = [1,2,3,4,5,6]
    result   = reordered(original)
    assert len(result) == len(original)

def test_same_elements_preserved():
    original = [1,2,3,4,5,6]
    result   = reordered(original)
    assert sorted(result) == sorted(original)

def test_first_element_unchanged():
    result = reordered([1,2,3,4,5])
    assert result[0] == 1

@pytest.mark.parametrize("vals, expected", [
    ([1,2,3,4],   [1,4,2,3]),
    ([1,2,3,4,5], [1,5,2,4,3]),
    ([1,2],       [1,2]),
    ([1,2,3],     [1,3,2]),
])
def test_parametrized(vals, expected):
    assert reordered(vals) == expected
