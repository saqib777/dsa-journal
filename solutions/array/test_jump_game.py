import pytest
from jump_game import can_jump, min_jumps


def test_can_jump_basic_true():
    assert can_jump([2, 3, 1, 1, 4]) == True

def test_can_jump_basic_false():
    assert can_jump([3, 2, 1, 0, 4]) == False

def test_can_jump_single():
    assert can_jump([0]) == True

def test_can_jump_two_reachable():
    assert can_jump([1, 0]) == True

def test_can_jump_two_unreachable():
    assert can_jump([0, 1]) == False

def test_can_jump_all_ones():
    assert can_jump([1, 1, 1, 1, 1]) == True

def test_can_jump_zero_in_middle():
    assert can_jump([1, 0, 1]) == False

def test_can_jump_large_first_jump():
    assert can_jump([5, 0, 0, 0, 0]) == True

def test_min_jumps_basic():
    assert min_jumps([2, 3, 1, 1, 4]) == 2

def test_min_jumps_alternate():
    assert min_jumps([2, 3, 0, 1, 4]) == 2

def test_min_jumps_one_step():
    assert min_jumps([1, 1, 1, 1]) == 3

def test_min_jumps_single():
    assert min_jumps([0]) == 0

def test_min_jumps_large_leap():
    assert min_jumps([10, 0, 0, 0, 0]) == 1

@pytest.mark.parametrize("nums, expected", [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
    ([1,0],       True),
    ([0,1],       False),
    ([0],         True),
])
def test_can_jump_parametrized(nums, expected):
    assert can_jump(nums) == expected
