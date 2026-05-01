import pytest
from two_sum_variants import (
    two_sum_sorted,
    two_sum_count_pairs,
    two_sum_all_pairs,
    four_sum,
)


def test_sorted_basic():
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]

def test_sorted_middle():
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]

def test_sorted_adjacent():
    assert two_sum_sorted([1, 2, 3, 4], 3) == [1, 2]

def test_sorted_not_found():
    assert two_sum_sorted([1, 2, 3], 10) == []

def test_count_pairs_basic():
    assert two_sum_count_pairs([1, 5, 3, 3, 3], 6) == 4

def test_count_pairs_none():
    assert two_sum_count_pairs([1, 2, 3], 10) == 0

def test_count_pairs_all():
    assert two_sum_count_pairs([1, 1, 1, 1], 2) == 6

def test_all_pairs_basic():
    result = two_sum_all_pairs([1, 1, 2, 2, 3, 4, 4, 5], 5)
    assert [1, 4] in result
    assert [2, 3] in result

def test_all_pairs_no_result():
    assert two_sum_all_pairs([1, 2, 3], 10) == []

def test_all_pairs_duplicates_handled():
    result = two_sum_all_pairs([1, 1, 1, 4], 5)
    assert result == [[1, 4]]

def test_four_sum_basic():
    result = four_sum([1, 0, -1, 0, -2, 2], 0)
    assert [-2, -1, 1, 2] in result
    assert [-2, 0, 0, 2]  in result
    assert [-1, 0, 0, 1]  in result

def test_four_sum_empty():
    assert four_sum([1, 2, 3], 100) == []

def test_four_sum_no_duplicates():
    result = four_sum([2, 2, 2, 2, 2], 8)
    assert result == [[2, 2, 2, 2]]

@pytest.mark.parametrize("nums, target, expected", [
    ([2,7,11,15], 9,  [1,2]),
    ([2,3,4],     6,  [1,3]),
    ([-1,0],      -1, [1,2]),
])
def test_sorted_parametrized(nums, target, expected):
    assert two_sum_sorted(nums, target) == expected
