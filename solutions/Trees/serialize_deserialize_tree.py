# Algorithm: BFS Level-Order Serialization
# Time Complexity:  O(n) — visit every node once
# Space Complexity: O(n) — queue and string storage

from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def serialize(root: TreeNode) -> str:
    """
    Encode a binary tree to a single string using BFS.
    Null nodes represented as 'N'.

    Example:
        Tree:    1
                / \\
               2   3
                   / \\
                  4   5
        Output: "1,2,3,N,N,4,5"
    """
    if not root:
        return "N"

    result = []
    queue  = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.value))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("N")

    # Trim trailing nulls for compact representation
    while result and result[-1] == "N":
        result.pop()

    return ",".join(result)


def deserialize(data: str) -> TreeNode:
    """
    Decode a string back to a binary tree.
    Reconstructs level by level using a queue.
    """
    if not data or data == "N":
        return None

    values = data.split(",")
    root   = TreeNode(int(values[0]))
    queue  = deque([root])
    i      = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] != "N":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] != "N":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root: TreeNode) -> list:
    """Level-order list for comparison in tests."""
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    while result and result[-1] is None:
        result.pop()
    return result


if __name__ == "__main__":
    root = TreeNode(1,
             TreeNode(2),
             TreeNode(3, TreeNode(4), TreeNode(5)))

    serialized = serialize(root)
    print(serialized)                         # "1,2,3,N,N,4,5"

    recovered = deserialize(serialized)
    print(tree_to_list(recovered))            # [1,2,3,4,5]
    print(serialize(recovered) == serialized) # True

    print(serialize(None))                    # "N"
    print(deserialize("N"))                   # None
