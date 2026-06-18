
import pytest
from majority_element import majority_element, majority_element_hashmap, majority_element_ii


def test_basic():
    assert majority_element([2,2,1,1,1,2,2]) == 2

def test_three_elements():
    assert majority_element([3,2,3]) == 3

def test_single_element():
    assert majority_element([1]) == 1

def test_all_same():
    assert majority_element([5,5,5,5]) == 5

def test_majority_at_start():
    assert majority_element([1,1,1,2,3]) == 1

def test_majority_at_end():
    assert majority_element([2,3,1,1,1]) == 1

def test_hashmap_matches():
    cases = [[2,2,1,1,1,2,2],[3,2,3],[1],[6,5,5]]
    for nums in cases:
        assert majority_element(nums) == majority_element_hashmap(nums)

def test_ii_basic():
    assert majority_element_ii([3,2,3]) == [3]

def test_ii_two_majorities():
    result = sorted(majority_element_ii([1,1,1,3,3,2,2,2]))
    assert result == [1,2]

def test_ii_no_majority():
    assert majority_element_ii([1,2,3,4]) == []

def test_ii_single_element():
    assert majority_element_ii([1]) == [1]

@pytest.mark.parametrize("nums, expected", [
    ([1,2,1,1,1],   1),
    ([7],           7),
    ([4,4,4,4,5],   4),
])
def test_parametrized(nums, expected):
    assert majority_element(nums) == expected
