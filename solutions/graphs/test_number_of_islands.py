import pytest
from number_of_islands import num_islands


def g(rows):
    return [list(r) for r in rows]


def test_one_island():
    assert num_islands(g(['11110','11010','11000','00000'])) == 1

def test_three_islands():
    assert num_islands(g(['11000','11000','00100','00011'])) == 3

def test_all_water():
    assert num_islands(g(['0000','0000'])) == 0

def test_all_land():
    assert num_islands(g(['111','111','111'])) == 1

def test_empty_grid():
    assert num_islands([]) == 0

def test_single_land():
    assert num_islands([['1']]) == 1

def test_single_water():
    assert num_islands([['0']]) == 0

def test_diagonal_not_connected():
    # Diagonal cells are NOT connected — each '1' is its own island
    assert num_islands(g(['10','01'])) == 2

def test_one_row():
    assert num_islands([['1','0','1','0','1']]) == 3

def test_one_column():
    assert num_islands([['1'],['0'],['1'],['0'],['1']]) == 3
