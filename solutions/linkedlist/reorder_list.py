# Algorithm: Find Middle + Reverse Second Half + Merge
# Time Complexity:  O(n) — three linear passes
# Space Complexity: O(1) — in-place, no extra list

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


def reorder_list(head: Node) -> None:
    """
    Reorder a linked list in-place from:
        L0 → L1 → L2 → ... → Ln
    to:
        L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

    Modifies list in-place. Returns None.

    Example:
        1 → 2 → 3 → 4      becomes  1 → 4 → 2 → 3
        1 → 2 → 3 → 4 → 5  becomes  1 → 5 → 2 → 4 → 3

    Approach — three steps:
    1. Find the middle using fast/slow pointers
    2. Reverse the second half
    3. Merge the two halves by interleaving
    """
    if not head or not head.next:
        return

    # Step 1: find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half
    second = slow.next
    slow.next = None   # cut the list
    prev = None
    while second:
        nxt         = second.next
        second.next = prev
        prev        = second
        second      = nxt
    second = prev   # head of reversed second half

    # Step 3: interleave first and reversed second half
    first = head
    while second:
        tmp1        = first.next
        tmp2        = second.next
        first.next  = second
        second.next = tmp1
        first       = tmp1
        second      = tmp2


def build(values: list) -> Node:
    if not values: return None
    head = Node(values[0]); cur = head
    for v in values[1:]: cur.next = Node(v); cur = cur.next
    return head

def to_list(head: Node) -> list:
    r = []
    while head: r.append(head.value); head = head.next
    return r


if __name__ == "__main__":
    h = build([1, 2, 3, 4])
    reorder_list(h)
    print(to_list(h))   # [1, 4, 2, 3]

    h = build([1, 2, 3, 4, 5])
    reorder_list(h)
    print(to_list(h))   # [1, 5, 2, 4, 3]
