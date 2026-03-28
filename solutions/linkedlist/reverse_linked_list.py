
# Algorithm: Iterative Pointer Reversal
# Time Complexity: O(n) - single pass through the linked list
# Space Complexity: O(1) - only three pointers used, no extra space

class Node:
    """Represents a single node in a linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head: Node) -> Node:
    """
    Given the head of a singly linked list, reverse it
    and return the new head.
    """
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def list_to_linkedlist(values: list) -> Node:
    """Helper: converts a Python list to a linked list, returns head."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def linkedlist_to_list(head: Node) -> list:
    """Helper: converts a linked list back to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result


if __name__ == "__main__":
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    print(linkedlist_to_list(reversed_head))  # [5, 4, 3, 2, 1]

    head = list_to_linkedlist([1, 2])
    reversed_head = reverse_linked_list(head)
    print(linkedlist_to_list(reversed_head))  # [2, 1]
