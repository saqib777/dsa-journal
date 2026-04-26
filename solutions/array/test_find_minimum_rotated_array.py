import pytest
from find_minimum_rotated_array import find_minimum, find_minimum_with_duplicates


def test_basic_rotated():
    assert find_minimum([3, 4, 5, 1, 2]) == 1

def test_rotated_more():
    assert find_minimum([4, 5, 6, 7, 0, 1, 2]) == 0

def test_no_rotation():
    assert find_minimum([11, 13, 15, 17]) == 11

def test_single_element():
    assert find_minimum([1]) == 1

def test_two_elements_rotated():
    assert find_minimum([2, 1]) == 1

def test_two_elements_not_rotated():
    assert find_minimum([1, 2]) == 1

def test_rotation_at_start():
    assert find_minimum([1, 2, 3, 4, 5]) == 1

def test_rotation_at_end():
    assert find_minimum([2, 3, 4, 5, 1]) == 1

def test_large_rotation():
    assert find_minimum([6, 7, 8, 9, 10, 1, 2, 3, 4, 5]) == 1

def test_duplicates_basic():
    assert find_minimum_with_duplicates([2, 2, 2, 0, 1]) == 0

def test_duplicates_no_rotation():
    assert find_minimum_with_duplicates([1, 3, 5]) == 1

def test_duplicates_all_same():
    assert find_minimum_with_duplicates([2, 2, 2, 2]) == 2

@pytest.mark.parametrize("nums, expected", [
    ([3, 1, 2], 1),
    ([5, 1, 2, 3, 4], 1),
    ([1], 1),
])
def test_parametrized(nums, expected):
    assert find_minimum(nums) == expected
