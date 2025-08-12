"""A simple Node class for a binary tree with a string representation."""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"""
        Node(val={self.val}, left={self.left}, right={self.right})
        """


tree = Node(
    0,
    Node(1, Node(3, Node(7), Node(8)), Node(4, Node(9), Node(10))),
    Node(2, Node(5, Node(11), Node(12)), Node(6, Node(13), Node(14))),
)
