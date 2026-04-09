# Algorithm: Floyd's Cycle Detection (Fast and Slow Pointers)
# Time Complexity:  O(n) — fast pointer laps slow pointer within n steps
# Space Complexity: O(1) — only two pointers used

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


def has_cycle(head: Node) -> bool:
    """
    Return True if the linked list contains a cycle.
    Uses Floyd's tortoise-and-hare algorithm.
    """
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True

    return False


def make_cycle_list(values: list, cycle_pos: int):
    """
    Helper: build a linked list and connect tail to node at cycle_pos.
    cycle_pos = -1 means no cycle.
    """
    if not values:
        return None
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos != -1:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0]


if __name__ == "__main__":
    head = make_cycle_list([3, 2, 0, -4], cycle_pos=1)
    print(has_cycle(head))   # True

    head = make_cycle_list([1, 2], cycle_pos=-1)
    print(has_cycle(head))   # False
