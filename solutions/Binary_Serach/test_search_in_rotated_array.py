import pytest
from search_in_rotated_array import search_rotated


def test_target_in_left_half():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 5) == 1

def test_target_in_right_half():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4

def test_target_not_found():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1

def test_single_element_found():
    assert search_rotated([1], 1) == 0

def test_single_element_not_found():
    assert search_rotated([1], 0) == -1

def test_two_elements_rotated():
    assert search_rotated([3, 1], 1) == 1

def test_no_rotation():
    assert search_rotated([1, 2, 3, 4, 5], 3) == 2

def test_target_at_pivot():
    assert search_rotated([6, 7, 1, 2, 3, 4, 5], 1) == 2

def test_target_is_largest():
    assert search_rotated([3, 4, 5, 1, 2], 5) == 2

def test_target_is_smallest():
    assert search_rotated([3, 4, 5, 1, 2], 1) == 3

@pytest.mark.parametrize("nums, target, expected", [
    ([1, 3], 3, 1),
    ([5, 1, 3], 3, 2),
    ([4, 5, 6, 7, 0, 1, 2], 6, 2),
])
def test_parametrized(nums, target, expected):
    assert search_rotated(nums, target) == expected
