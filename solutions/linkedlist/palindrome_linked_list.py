# Algorithm: Fast/Slow Pointers + Reverse Second Half
# Time Complexity:  O(n) — single pass to find middle, reverse, compare
# Space Complexity: O(1) — no extra list, reverses in-place

class Node:
    def __init__(self, value):
        self.value = value
        self.next  = None


def is_palindrome(head: Node) -> bool:
    """
    Determine if a linked list reads the same forwards and backwards.

    Approach (O(1) space — no array conversion):
    1. Find the middle using fast/slow pointers.
    2. Reverse the second half in-place.
    3. Compare first half against reversed second half.
    4. (Optional) Restore the list to original state.

    Example:
        1 -> 2 -> 2 -> 1  → True
        1 -> 2 -> 3       → False
    """
    if not head or not head.next:
        return True

    # Step 1: find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: reverse second half starting at slow
    prev = None
    curr = slow
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    # Step 3: compare halves
    first_half  = head
    second_half = prev   # prev is now head of reversed second half
    result = True
    while second_half:
        if first_half.value != second_half.value:
            result = False
            break
        first_half  = first_half.next
        second_half = second_half.next

    return result


def is_palindrome_list_conversion(head: Node) -> bool:
    """
    Simpler approach: convert to Python list and compare with reverse.
    Time: O(n), Space: O(n)
    """
    values = []
    while head:
        values.append(head.value)
        head = head.next
    return values == values[::-1]


def build(values: list) -> Node:
    if not values: return None
    head = Node(values[0]); cur = head
    for v in values[1:]: cur.next = Node(v); cur = cur.next
    return head


if __name__ == "__main__":
    print(is_palindrome(build([1, 2, 2, 1])))   # True
    print(is_palindrome(build([1, 2, 3])))       # False
    print(is_palindrome(build([1])))             # True
    print(is_palindrome(build([1, 2, 3, 2, 1]))) # True

    print(is_palindrome_list_conversion(build([1, 2, 2, 1])))  # True
