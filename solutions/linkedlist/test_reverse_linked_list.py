import pytest
from reverse_linked_list import reverse_linked_list, list_to_linkedlist, linkedlist_to_list


def test_basic_reverse():
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    assert linkedlist_to_list(reverse_linked_list(head)) == [5, 4, 3, 2, 1]

def test_two_elements():
    head = list_to_linkedlist([1, 2])
    assert linkedlist_to_list(reverse_linked_list(head)) == [2, 1]

def test_single_element():
    head = list_to_linkedlist([1])
    assert linkedlist_to_list(reverse_linked_list(head)) == [1]

def test_empty_list():
    assert reverse_linked_list(None) is None

def test_already_reversed():
    head = list_to_linkedlist([5, 4, 3, 2, 1])
    assert linkedlist_to_list(reverse_linked_list(head)) == [1, 2, 3, 4, 5]

def test_same_values():
    head = list_to_linkedlist([7, 7, 7])
    assert linkedlist_to_list(reverse_linked_list(head)) == [7, 7, 7]
