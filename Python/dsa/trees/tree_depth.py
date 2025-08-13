"""Given a binary tree, find its max depth."""

from dsa.trees.node import Node, tree


def max_depth(node: Node | None) -> int:
    """Use a recursive approach,
    if we're passed None, then just return zero,
    otherwise return the max depth of either
    the left or the right plus 1 (to represent the current node)
    """
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))


depth = max_depth(tree)
print(depth)
