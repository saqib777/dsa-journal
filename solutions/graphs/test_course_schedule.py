import pytest
from course_schedule import can_finish, find_order


def test_can_finish_basic():
    assert can_finish(2, [[1, 0]]) == True

def test_cycle_detected():
    assert can_finish(2, [[1, 0], [0, 1]]) == False

def test_no_prerequisites():
    assert can_finish(5, []) == True

def test_single_course():
    assert can_finish(1, []) == True

def test_longer_chain():
    assert can_finish(4, [[1,0],[2,1],[3,2]]) == True

def test_cycle_in_chain():
    assert can_finish(4, [[1,0],[2,1],[3,2],[0,3]]) == False

def test_disconnected_cycle():
    assert can_finish(6, [[1,0],[2,1],[3,4],[4,5],[5,3]]) == False

def test_find_order_basic():
    order = find_order(2, [[1, 0]])
    assert order.index(0) < order.index(1)

def test_find_order_impossible():
    assert find_order(2, [[1, 0], [0, 1]]) == []

def test_find_order_no_prereqs():
    order = find_order(3, [])
    assert sorted(order) == [0, 1, 2]

def test_find_order_diamond():
    order = find_order(4, [[1,0],[2,0],[3,1],[3,2]])
    assert order.index(0) < order.index(1)
    assert order.index(0) < order.index(2)
    assert order.index(1) < order.index(3)
    assert order.index(2) < order.index(3)

@pytest.mark.parametrize("n, prereqs, expected", [
    (2, [[1,0]], True),
    (3, [[1,0],[2,1]], True),
    (3, [[0,1],[1,2],[2,0]], False),
])
def test_parametrized(n, prereqs, expected):
    assert can_finish(n, prereqs) == expected
