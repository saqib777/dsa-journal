import pytest
from unique_paths import (
    unique_paths,
    unique_paths_optimised,
    unique_paths_with_obstacles,
    unique_paths_math,
)


def test_basic_3x7():
    assert unique_paths(3, 7) == 28

def test_basic_3x2():
    assert unique_paths(3, 2) == 3

def test_single_row():
    assert unique_paths(1, 10) == 1

def test_single_col():
    assert unique_paths(10, 1) == 1

def test_single_cell():
    assert unique_paths(1, 1) == 1

def test_square():
    assert unique_paths(3, 3) == 6

def test_all_methods_agree():
    for m in range(1, 8):
        for n in range(1, 8):
            dp   = unique_paths(m, n)
            opt  = unique_paths_optimised(m, n)
            math = unique_paths_math(m, n)
            assert dp == opt == math, f"Mismatch at m={m}, n={n}"

def test_obstacles_basic():
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    assert unique_paths_with_obstacles(grid) == 2

def test_obstacles_start_blocked():
    grid = [[1,0],[0,0]]
    assert unique_paths_with_obstacles(grid) == 0

def test_obstacles_end_blocked():
    grid = [[0,0],[0,1]]
    assert unique_paths_with_obstacles(grid) == 0

def test_obstacles_none():
    grid = [[0,0,0],[0,0,0]]
    assert unique_paths_with_obstacles(grid) == 3

def test_obstacles_all_right_then_down():
    grid = [[0,0],[0,0],[0,0]]
    assert unique_paths_with_obstacles(grid) == 3

@pytest.mark.parametrize("m, n, expected", [
    (2, 2, 2),
    (3, 3, 6),
    (1, 1, 1),
    (4, 4, 20),
])
def test_parametrized(m, n, expected):
    assert unique_paths(m, n) == expected
