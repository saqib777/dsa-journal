
import pytest
from maximum_product_subarray import max_product


def test_basic():
    assert max_product([2, 3, -2, 4]) == 6

def test_with_zero():
    assert max_product([-2, 0, -1]) == 0

def test_two_negatives():
    assert max_product([-2, 3, -4]) == 24

def test_single_element():
    assert max_product([5]) == 5

def test_single_negative():
    assert max_product([-3]) == -3

def test_all_negatives():
    assert max_product([-1, -2, -3, -4]) == 24

def test_all_positive():
    assert max_product([1, 2, 3, 4]) == 24

def test_contains_zero():
    assert max_product([0, 2, 3]) == 6
