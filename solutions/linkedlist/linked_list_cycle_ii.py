# Algorithm: Floyd's Cycle Detection — Find Cycle Entry Point
# Time Complexity:  O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


def detect_cycle_entry(head: Node) -> Node:
    """
    Find the node where the cycle begins in a linked list.
    Returns None if no cycle.

    Phase 1: Detect cycle using fast and slow pointers.
    Phase 2: Find entry point.

    Mathematical proof of Phase 2:
    Let F = distance from head to cycle entry.
    Let C = cycle length.
    When slow and fast meet inside the cycle:
        slow traveled: F + a   (a = distance inside cycle)
        fast traveled: F + a + n*C

    Since fast = 2 * slow:
        2(F + a) = F + a + n*C
        F + a    = n*C
        F        = n*C - a

    Moving one pointer to head and advancing both by 1:
    they meet exactly at the cycle entry.
    """
    slow = fast = head

    # Phase 1: detect meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None   # no cycle

    # Phase 2: find entry
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow


def build_cycle_list(values: list[int], cycle_pos: int):
    """Build linked list with cycle at cycle_pos. -1 = no cycle."""
    if not values:
        return None
    nodes = [Node(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]
    return nodes[0], nodes


if __name__ == "__main__":
    head, nodes = build_cycle_list([3, 2, 0, -4], cycle_pos=1)
    entry = detect_cycle_entry(head)
    print(entry.value if entry else None)   # 2

    head, nodes = build_cycle_list([1, 2], cycle_pos=0)
    entry = detect_cycle_entry(head)
    print(entry.value if entry else None)   # 1

    head, nodes = build_cycle_list([1], cycle_pos=-1)
    print(detect_cycle_entry(head))         # None
