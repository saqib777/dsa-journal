import pytest
from kth_largest_element import kth_largest_heap, kth_largest_quickselect


def test_heap_basic():
    assert kth_largest_heap([3, 2, 1, 5, 6, 4], 2) == 5

def test_heap_with_duplicates():
    assert kth_largest_heap([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

def test_heap_k_equals_1():
    assert kth_largest_heap([3, 2, 1, 5, 6, 4], 1) == 6

def test_heap_k_equals_n():
    assert kth_largest_heap([3, 2, 1, 5, 6, 4], 6) == 1

def test_heap_single_element():
    assert kth_largest_heap([1], 1) == 1

def test_heap_all_same():
    assert kth_largest_heap([5, 5, 5, 5], 2) == 5

def test_heap_negative_numbers():
    assert kth_largest_heap([-1, -2, -3, -4], 2) == -2

def test_quickselect_basic():
    assert kth_largest_quickselect([3, 2, 1, 5, 6, 4], 2) == 5

def test_quickselect_duplicates():
    assert kth_largest_quickselect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

def test_quickselect_k1():
    assert kth_largest_quickselect([3, 2, 1, 5, 6, 4], 1) == 6

def test_both_agree():
    cases = [
        ([3,2,1,5,6,4], 2),
        ([3,2,3,1,2,4,5,5,6], 4),
        ([1,2,3,4,5], 3),
        ([-1,-5,3,7,2], 1),
    ]
    for nums, k in cases:
        assert kth_largest_heap(list(nums), k) == kth_largest_quickselect(list(nums), k)

@pytest.mark.parametrize("nums, k, expected", [
    ([1], 1, 1),
    ([2, 1], 2, 1),
    ([7, 6, 5, 4, 3, 2, 1], 5, 3),
])
def test_parametrized(nums, k, expected):
    assert kth_largest_heap(nums, k) == expected
