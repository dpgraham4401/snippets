"""
Given a tree of nodes (see class below), invert the binary tree
so that all nodes on the left are swapped to the right, and vice versa.
"""

from dsa.trees.node import Node, tree


def invert_tree(node: Node | None):
    if not node:
        return None

    tmp = node.left
    node.left = node.right
    node.right = tmp

    invert_tree(node.left)
    invert_tree(node.right)
    return node


invert_tree(tree)
print(tree)
