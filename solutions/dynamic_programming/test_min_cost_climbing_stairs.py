
import pytest
from min_cost_climbing_stairs import (
    min_cost_climbing_stairs,
    min_cost_climbing_stairs_dp,
    min_cost_with_path,
)


def test_basic_three_steps():
    assert min_cost_climbing_stairs([10, 15, 20]) == 15

def test_longer_example():
    assert min_cost_climbing_stairs([1,100,1,1,1,100,1,1,100,1]) == 6

def test_two_steps_pick_cheaper():
    assert min_cost_climbing_stairs([1, 100]) == 1

def test_two_steps_pick_cheaper_reversed():
    assert min_cost_climbing_stairs([100, 1]) == 1

def test_all_same_cost():
    assert min_cost_climbing_stairs([5, 5, 5, 5]) == 10

def test_single_step():
    assert min_cost_climbing_stairs([7]) == 7

def test_empty():
    assert min_cost_climbing_stairs([]) == 0

def test_both_implementations_agree():
    cases = [
        [10, 15, 20],
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
        [0, 0, 0, 0],
        [1, 2, 3, 4, 5],
    ]
    for cost in cases:
        assert min_cost_climbing_stairs(cost) == min_cost_climbing_stairs_dp(cost)

def test_path_correct_cost():
    total, path = min_cost_with_path([10, 15, 20])
    assert total == 15
    assert len(path) >= 1

def test_path_steps_within_bounds():
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    total, path = min_cost_with_path(cost)
    assert total == 6
    assert all(0 <= p < len(cost) for p in path)

def test_zeros_cost():
    assert min_cost_climbing_stairs([0, 0, 0, 0]) == 0

@pytest.mark.parametrize("cost, expected", [
    ([10,15,20],  15),
    ([1,100],      1),
    ([5,5],        5),
    ([1,2,3],      2),
])
def test_parametrized(cost, expected):
    assert min_cost_climbing_stairs(cost) == expected
