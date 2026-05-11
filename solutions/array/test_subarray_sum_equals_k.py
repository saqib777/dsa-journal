import pytest
from subarray_sum_equals_k import (
    subarray_sum,
    max_subarray_sum_k,
    subarray_sum_divisible_by_k,
)


def test_basic_two():
    assert subarray_sum([1, 1, 1], 2) == 2

def test_multiple_paths():
    assert subarray_sum([1, 2, 3], 3) == 2

def test_negative_numbers():
    assert subarray_sum([-1, -1, 1], 0) == 1

def test_single_element_match():
    assert subarray_sum([3], 3) == 1

def test_single_element_no_match():
    assert subarray_sum([3], 5) == 0

def test_empty():
    assert subarray_sum([], 0) == 0

def test_all_zeros():
    assert subarray_sum([0, 0, 0, 0], 0) == 10

def test_k_zero_with_negatives():
    assert subarray_sum([1, -1, 1, -1], 0) == 4

def test_max_length_basic():
    assert max_subarray_sum_k([1, -1, 5, -2, 3], 3) == 4

def test_max_length_negative():
    assert max_subarray_sum_k([-2, -1, 2, 1], 1) == 2

def test_max_length_no_match():
    assert max_subarray_sum_k([1, 2, 3], 10) == 0

def test_divisible_basic():
    assert subarray_sum_divisible_by_k([4,5,0,-2,-3,1], 5) == 7

def test_divisible_single():
    assert subarray_sum_divisible_by_k([5], 5) == 1

@pytest.mark.parametrize("nums, k, expected", [
    ([1,1,1],   2, 2),
    ([1,2,3],   3, 2),
    ([0,0,0,0], 0, 10),
    ([1],       1, 1),
    ([1],       2, 0),
])
def test_parametrized(nums, k, expected):
    assert subarray_sum(nums, k) == expected
