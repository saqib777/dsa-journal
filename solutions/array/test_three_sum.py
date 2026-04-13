import pytest
from three_sum import three_sum


def sorted_result(result):
    """Sort each triplet and sort triplets for deterministic comparison."""
    return sorted([sorted(t) for t in result])


def test_basic():
    assert sorted_result(three_sum([-1, 0, 1, 2, -1, -4])) == [
        [-1, -1, 2],
        [-1,  0, 1],
    ]

def test_all_zeros():
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]

def test_no_triplet():
    assert three_sum([1, 2, -2, -1]) == []

def test_empty():
    assert three_sum([]) == []

def test_two_elements():
    assert three_sum([0, 1]) == []

def test_duplicates_handled():
    assert sorted_result(three_sum([-2, 0, 0, 2, 2])) == [[-2, 0, 2]]

def test_all_positive():
    assert three_sum([1, 2, 3, 4]) == []

def test_all_negative():
    assert three_sum([-4, -3, -2, -1]) == []

@pytest.mark.parametrize("nums, expected", [
    ([0, 0, 0, 0], [[0, 0, 0]]),
    ([-1, -1, 2], [[-1, -1, 2]]),
])
def test_parametrized(nums, expected):
    assert sorted_result(three_sum(nums)) == sorted_result(expected)
