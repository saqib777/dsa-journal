# Algorithm: DFS with Valid Range (Min/Max Boundaries)
# Time Complexity:  O(n) — every node visited once
# Space Complexity: O(h) — h = height of tree (recursion stack)

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def is_valid_bst(root: TreeNode) -> bool:
    """
    Return True if the binary tree is a valid Binary Search Tree.
    BST rule: left subtree < node < right subtree at every level.
    """
    def validate(node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (validate(node.left,  min_val,    node.value) and
                validate(node.right, node.value, max_val))

    return validate(root, float('-inf'), float('inf'))


if __name__ == "__main__":
    #   Valid BST        Invalid BST
    #       2                 5
    #      / \               / \
    #     1   3             1   4
    #                          / \
    #                         3   6
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    print(is_valid_bst(valid))   # True

    invalid = TreeNode(5,
                TreeNode(1),
                TreeNode(4, TreeNode(3), TreeNode(6)))
    print(is_valid_bst(invalid)) # False
