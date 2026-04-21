import pytest
from house_robber import rob


def test_basic_odd():
    assert rob([1, 2, 3, 1]) == 4

def test_basic_even():
    assert rob([2, 7, 9, 3, 1]) == 12

def test_two_houses():
    assert rob([2, 1, 1, 2]) == 4

def test_single_house():
    assert rob([5]) == 5

def test_empty():
    assert rob([]) == 0

def test_two_elements():
    assert rob([3, 10]) == 10

def test_all_equal():
    assert rob([5, 5, 5, 5, 5]) == 15

def test_increasing():
    assert rob([1, 2, 3, 4, 5]) == 9

def test_large_values():
    assert rob([100, 1, 100, 1, 100]) == 300

@pytest.mark.parametrize("nums, expected", [
    ([2, 3, 2], 3),
    ([1, 3, 1], 3),
    ([0, 0, 0], 0),
])
def test_parametrized(nums, expected):
    assert rob(nums) == expected
