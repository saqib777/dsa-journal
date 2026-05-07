import pytest
from knapsack_01 import knapsack_01, knapsack_01_optimised, knapsack_with_items


def test_basic():
    assert knapsack_01([1,3,4,5],[1,4,5,7],7) == 9

def test_zero_capacity():
    assert knapsack_01([1,2,3],[10,20,30],0) == 0

def test_single_item_fits():
    assert knapsack_01([3],[10],5) == 10

def test_single_item_too_heavy():
    assert knapsack_01([6],[10],5) == 0

def test_all_items_fit():
    assert knapsack_01([1,1,1],[5,5,5],10) == 15

def test_no_items():
    assert knapsack_01([],[],10) == 0

def test_optimised_matches_2d():
    cases = [
        ([1,3,4,5],[1,4,5,7],7),
        ([2,3,4,5],[3,4,5,6],5),
        ([1,1,1],[5,5,5],2),
        ([10],[50],9),
    ]
    for w, v, c in cases:
        assert knapsack_01(w,v,c) == knapsack_01_optimised(w,v,c)

def test_item_reconstruction_value():
    val, items = knapsack_with_items([1,3,4,5],[1,4,5,7],7)
    assert val == 9

def test_item_reconstruction_valid():
    weights = [1,3,4,5]; values = [1,4,5,7]; capacity = 7
    val, items = knapsack_with_items(weights, values, capacity)
    total_w = sum(weights[i] for i in items)
    total_v = sum(values[i]  for i in items)
    assert total_w <= capacity
    assert total_v == val

def test_large_capacity():
    assert knapsack_01([2,3,4],[3,4,5],100) == 12

@pytest.mark.parametrize("w,v,cap,expected", [
    ([1,2,3],[6,10,12],5,22),
    ([1],[1],1,1),
    ([5],[10],4,0),
    ([2,3],[3,4],5,7),
])
def test_parametrized(w,v,cap,expected):
    assert knapsack_01(w,v,cap) == expected
