"""
Data Structures :: AVL Tree
"""


class Node:
    """Node class to keep track of
    the data internal to individual nodes.
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class AVLTree:
    """A tree class to keep track of things like the
    balance factor and the rebalancing logic.
    """

    def __init__(self, node=None):
        self.node = node
        # init height to -1 because of 0-indexing
        self.height = -1
        self.balance = 0

    def display(self, level=0, pref=""):
        """Display the whole tree. Uses recursive def."""
        self.update_height()  # Update height before balancing
        self.update_balance()

        if self.node != None:
            print(
                "-" * level * 2,
                pref,
                self.node.key,
                f"[{self.height}:{self.balance}]",
                "L" if self.height == 0 else " ",
            )
            if self.node.left != None:
                self.node.left.display(level + 1, "<")
            if self.node.right != None:
                self.node.right.display(level + 1, ">")

    def update_height(self):
        """Computes the maximum number of levels there are
        in the tree.
        """
        pass

    def update_balance(self):
        """Updates the balance factor on the AVLTree class."""
        pass

    def left_rotate(self):
        """Perform a left rotation, making the right child of this
        node the parent and making the old parent the left child
        of the new parent. 
        """
        pass

    def right_rotate(self):
        """Perform a right rotation, making the left child of this
        node the parent and making the old parent the right child
        of the new parent. 
        """
        pass

    def rebalance(self):
        """Sets in motion the rebalancing logic to ensure the
        tree is balanced such that the balance factor is
        1 or -1.
        """
        pass

    def insert(self, key):
        """Uses the same insertion logic as a binary search tree
        after the value is inserted, we need to check to see
        if we need to rebalance.
        """
        pass
