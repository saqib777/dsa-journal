import pytest
from best_time_to_buy_sell_stock import max_profit


def test_basic_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

def test_no_profit_descending():
    assert max_profit([7, 6, 4, 3, 1]) == 0

def test_two_elements_profit():
    assert max_profit([1, 2]) == 1

def test_two_elements_no_profit():
    assert max_profit([2, 1]) == 0

def test_single_element():
    assert max_profit([5]) == 0

def test_empty_array():
    assert max_profit([]) == 0

def test_all_same_price():
    assert max_profit([3, 3, 3, 3]) == 0

def test_profit_at_end():
    assert max_profit([1, 2, 3, 4, 5]) == 4
