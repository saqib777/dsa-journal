# Algorithm: Recursive Divide and Conquer
# Time Complexity:  O(n) with hash map | O(n^2) naive
# Space Complexity: O(n) — hash map + recursion stack

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right


def build_from_preorder_inorder(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Reconstruct binary tree from preorder and inorder traversals.

    Key insight:
    - preorder[0] is always the root
    - Find root in inorder → everything left is left subtree,
      everything right is right subtree
    - Recurse on each half

    Hash map stores inorder index for O(1) root lookup.
    """
    inorder_index = {val: i for i, val in enumerate(inorder)}
    pre_idx       = [0]

    def build(left: int, right: int) -> TreeNode:
        if left > right:
            return None
        root_val          = preorder[pre_idx[0]]
        pre_idx[0]       += 1
        node              = TreeNode(root_val)
        mid               = inorder_index[root_val]
        node.left         = build(left, mid - 1)
        node.right        = build(mid + 1, right)
        return node

    return build(0, len(inorder) - 1)


def build_from_postorder_inorder(inorder: list[int], postorder: list[int]) -> TreeNode:
    """
    Reconstruct binary tree from postorder and inorder traversals.

    Key insight:
    - postorder[-1] is always the root
    - Same divide strategy as preorder/inorder but read postorder right to left
    """
    inorder_index = {val: i for i, val in enumerate(inorder)}
    post_idx      = [len(postorder) - 1]

    def build(left: int, right: int) -> TreeNode:
        if left > right:
            return None
        root_val        = postorder[post_idx[0]]
        post_idx[0]    -= 1
        node            = TreeNode(root_val)
        mid             = inorder_index[root_val]
        node.right      = build(mid + 1, right)
        node.left       = build(left, mid - 1)
        return node

    return build(0, len(inorder) - 1)


def tree_to_inorder(root: TreeNode) -> list[int]:
    """Helper: inorder traversal for verification."""
    result = []
    def traverse(node):
        if not node: return
        traverse(node.left)
        result.append(node.value)
        traverse(node.right)
    traverse(root)
    return result


def tree_to_preorder(root: TreeNode) -> list[int]:
    """Helper: preorder traversal for verification."""
    result = []
    def traverse(node):
        if not node: return
        result.append(node.value)
        traverse(node.left)
        traverse(node.right)
    traverse(root)
    return result


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder  = [9, 3, 15, 20, 7]

    root = build_from_preorder_inorder(preorder, inorder)
    print(tree_to_inorder(root))   # [9,3,15,20,7]
    print(tree_to_preorder(root))  # [3,9,20,15,7]

    postorder = [9, 15, 7, 20, 3]
    root2 = build_from_postorder_inorder(inorder, postorder)
    print(tree_to_inorder(root2))  # [9,3,15,20,7]
