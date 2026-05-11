import pytest
from trapping_rain_water import trap, trap_dp


def test_basic():
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6

def test_basic_2():
    assert trap([4,2,0,3,2,5]) == 9

def test_single():
    assert trap([1,0,1]) == 1

def test_larger():
    assert trap([3,0,0,2,0,4]) == 10

def test_empty():
    assert trap([]) == 0

def test_single_bar():
    assert trap([5]) == 0

def test_two_bars():
    assert trap([5, 3]) == 0

def test_flat():
    assert trap([3,3,3,3]) == 0

def test_valley():
    assert trap([5,0,5]) == 5

def test_ascending():
    assert trap([1,2,3,4,5]) == 0

def test_descending():
    assert trap([5,4,3,2,1]) == 0

def test_both_agree():
    cases = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5],
        [3,0,0,2,0,4],
        [1,0,1],
        [],
        [5],
    ]
    for h in cases:
        assert trap(list(h)) == trap_dp(list(h))

@pytest.mark.parametrize("height, expected", [
    ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
    ([4,2,0,3,2,5],              9),
    ([1,0,1],                    1),
    ([3,0,0,2,0,4],             10),
    ([5,3],                      0),
])
def test_parametrized(height, expected):
    assert trap(height) == expected
