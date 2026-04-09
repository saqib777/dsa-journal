
import pytest
from detect_cycle import has_cycle, make_cycle_list


def test_cycle_exists():
    head = make_cycle_list([3, 2, 0, -4], cycle_pos=1)
    assert has_cycle(head) == True

def test_no_cycle():
    head = make_cycle_list([1, 2], cycle_pos=-1)
    assert has_cycle(head) == False

def test_single_node_no_cycle():
    head = make_cycle_list([1], cycle_pos=-1)
    assert has_cycle(head) == False

def test_single_node_self_cycle():
    head = make_cycle_list([1], cycle_pos=0)
    assert has_cycle(head) == True

def test_empty_list():
    assert has_cycle(None) == False

def test_tail_connects_to_head():
    head = make_cycle_list([1, 2, 3, 4, 5], cycle_pos=0)
    assert has_cycle(head) == True

def test_long_list_no_cycle():
    head = make_cycle_list(list(range(100)), cycle_pos=-1)
    assert has_cycle(head) == False
