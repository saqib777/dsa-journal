import pytest
from merge_intervals import merge_intervals, insert_interval


def test_basic_merge():
    assert merge_intervals([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]

def test_touching_intervals():
    assert merge_intervals([[1,4],[4,5]]) == [[1,5]]

def test_contained_interval():
    assert merge_intervals([[1,4],[2,3]]) == [[1,4]]

def test_no_overlap():
    assert merge_intervals([[1,2],[3,4],[5,6]]) == [[1,2],[3,4],[5,6]]

def test_all_overlap():
    assert merge_intervals([[1,4],[2,5],[3,6]]) == [[1,6]]

def test_single_interval():
    assert merge_intervals([[1,5]]) == [[1,5]]

def test_empty():
    assert merge_intervals([]) == []

def test_unsorted_input():
    assert merge_intervals([[3,4],[1,2],[2,3]]) == [[1,4]]

def test_insert_basic():
    assert insert_interval([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]

def test_insert_no_overlap():
    assert insert_interval([[1,2],[5,6]], [3,4]) == [[1,2],[3,4],[5,6]]

def test_insert_covers_all():
    assert insert_interval([[1,2],[3,5],[6,7]], [1,8]) == [[1,8]]

def test_insert_empty_list():
    assert insert_interval([], [1,5]) == [[1,5]]

def test_insert_at_start():
    assert insert_interval([[3,5],[6,9]], [1,2]) == [[1,2],[3,5],[6,9]]

def test_insert_at_end():
    assert insert_interval([[1,3],[4,6]], [8,10]) == [[1,3],[4,6],[8,10]]

@pytest.mark.parametrize("intervals, expected", [
    ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
    ([[1,4],[4,5]],               [[1,5]]),
    ([[1,4],[2,3]],               [[1,4]]),
    ([[1,2],[3,4]],               [[1,2],[3,4]]),
])
def test_parametrized(intervals, expected):
    assert merge_intervals(intervals) == expected
