"""
Given a tree of nodes (see class below), invert the binary tree
so that all nodes on the left are swapped to the right, and vice versa.
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"""
        Node(val={self.val}, left={self.left}, right={self.right})
        """


root = Node(
    0,
    Node(1, Node(3, Node(7), Node(8)), Node(4, Node(9), Node(10))),
    Node(2, Node(5, Node(11), Node(12)), Node(6, Node(13), Node(14))),
)


def invert_tree(node: Node | None):
    if not node:
        return None

    tmp = node.left
    node.left = node.right
    node.right = tmp

    invert_tree(node.left)
    invert_tree(node.right)
    return node


invert_tree(root)
print(root)
