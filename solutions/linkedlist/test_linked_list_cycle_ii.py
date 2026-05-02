import pytest
from linked_list_cycle_ii import detect_cycle_entry, build_cycle_list


def test_cycle_entry_at_index_1():
    head, nodes = build_cycle_list([3, 2, 0, -4], cycle_pos=1)
    entry = detect_cycle_entry(head)
    assert entry is nodes[1]
    assert entry.value == 2

def test_cycle_entry_at_index_0():
    head, nodes = build_cycle_list([1, 2], cycle_pos=0)
    entry = detect_cycle_entry(head)
    assert entry is nodes[0]
    assert entry.value == 1

def test_no_cycle():
    head, _ = build_cycle_list([1, 2, 3, 4], cycle_pos=-1)
    assert detect_cycle_entry(head) is None

def test_single_node_no_cycle():
    head, _ = build_cycle_list([1], cycle_pos=-1)
    assert detect_cycle_entry(head) is None

def test_single_node_self_cycle():
    head, nodes = build_cycle_list([1], cycle_pos=0)
    entry = detect_cycle_entry(head)
    assert entry is nodes[0]

def test_cycle_at_last_node():
    head, nodes = build_cycle_list([1, 2, 3, 4, 5], cycle_pos=4)
    entry = detect_cycle_entry(head)
    assert entry is nodes[4]

def test_full_cycle():
    head, nodes = build_cycle_list([1, 2, 3, 4, 5], cycle_pos=0)
    entry = detect_cycle_entry(head)
    assert entry is nodes[0]

def test_large_list_cycle():
    head, nodes = build_cycle_list(list(range(100)), cycle_pos=50)
    entry = detect_cycle_entry(head)
    assert entry is nodes[50]

def test_none_input():
    assert detect_cycle_entry(None) is None
