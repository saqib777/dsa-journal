import pytest
from climbing_stairs import climb_stairs


def test_one_step():
    assert climb_stairs(1) == 1

def test_two_steps():
    assert climb_stairs(2) == 2

def test_three_steps():
    assert climb_stairs(3) == 3

def test_five_steps():
    assert climb_stairs(5) == 8

def test_ten_steps():
    assert climb_stairs(10) == 89

def test_large():
    assert climb_stairs(45) == 1836311903

@pytest.mark.parametrize("n, expected", [
    (1, 1), (2, 2), (3, 3), (4, 5), (5, 8), (6, 13)
])
def test_parametrized(n, expected):
    assert climb_stairs(n) == expected
