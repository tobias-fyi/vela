"""
Data Structures :: Binary search tree
"""


# import sys

# sys.path.append("../queue_and_stack")
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        """Implementation of a binary search tree.
        Each node can be considered a leaf and a complete tree.
        """
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """Inserts the given value into the tree."""
        if value < self.value:
            if self.left is None:  # Base case: empty leaf
                self.left = BinarySearchTree(value)
            else:  # Recursive case
                self.left.insert(value)
        else:
            if self.right is None:  # Base case: empty leaf
                self.right = BinarySearchTree(value)
            else:  # If exists: recur into right
                self.right.insert(value)

    def contains(self, target):
        """Searches the tree for the target value.
        
        :param target : Target value.
        :return contains (Bool) : Indicates if target is in tree.
        """
        # Compare value to target
        if self.value == target:
            return True
        # === Go left ===
        if target < self.value:
            if self.left is None:  # If left is None, return None (base case)
                return False
            else:  # If left exists, recur left
                return self.left.contains(target)
        # === Go right ===
        else:
            if self.right is None:  # If right is None, return None (base case)
                return False
            else:  # If right exists, recur right
                return self.right.contains(target)

    def get_max(self):
        """Return the maximum value found in the tree."""
        if self.right is None:  # Rightmost value is maximum
            return self.value
        else:
            return self.right.get_max()

    def for_each(self, cb):
        """Calls the function `cb()` on the value of each node.
        You may use a recursive or iterative approach.
        """
        cb(self.value)  # Call function on current node's value
        # === Go left === #
        if self.left is not None:  # Left exists, recur left
            self.left.for_each(cb)
        # === Go right === #
        if self.right is not None:  # Right exists, recur right
            self.right.for_each(cb)

    # ====== DAY 2 Project ====== #

    def in_order_print(self, node):
        """Prints all the values in order from low to high.
        Hint: Use a recursive, depth first traversal
        """
        # Go left
        if self.left:
            # If left exists, call func on it
            self.left.in_order_print(self.left)
        # Print self after lower values are done
        # And before higher values are done
        print(self.value)
        # Go right
        if self.right:
            # If right exists, call func on it
            self.right.in_order_print(self.right)

    # def bft_print(self, node):
    #     """Prints the value of every node, starting with the given node,
    #     in an iterative breadth first traversal
    #     """
    #     q = Queue()  # Create queue
    #     q.enqueue(node)  # Add root (bst/node) to queue
    #     # while queue is not empty
    #     while q.len() > 0:
    #         # Pop current node off the queue to process
    #         current_node = q.dequeue()
    #         # DO THE THING (print)
    #         print(current_node.value)
    #         # Add children of root to queue
    #         if current_node.left:
    #             q.enqueue(current_node.left)
    #         if current_node.right:
    #             q.enqueue(current_node.right)

    # def dft_print(self, node):
    #     """Prints the value of every node, starting with the given node,
    #     in an iterative depth first traversal.
    #     """
    #     stack = Stack()  # Instantiate stack
    #     stack.push(node)  # Add root (node) to stack
    #     # While stack is not empty
    #     while stack.len() > 0:
    #         # Node = pop the top of the stack
    #         current_node = stack.pop()
    #         print(current_node.value)  # DO THE THING!
    #         # Add any existing children of current node to stack
    #         if current_node.right:
    #             stack.push(current_node.right)
    #         if current_node.left:
    #             stack.push(current_node.left)

    # ====== STRETCH Goals ====== #
    # Note: Research may be required

    def pre_order_dft(self, node):
        """Prints Pre-order recursive DFT."""
        # Process self
        print(node.value)
        # Process left
        if node.left:
            node.left.pre_order_dft(node.left)
        # Process right
        if node.right:
            node.right.pre_order_dft(node.right)

    def post_order_dft(self, node):
        """Prints Post-order recursive DFT."""
        # Process left
        if node.left:
            node.left.post_order_dft(node.left)
        # Process right
        if node.right:
            node.right.post_order_dft(node.right)
        # Process self
        print(node.value)


# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# print("In order:")
# bst.in_order_print(bst)

# print("\nDepth-first:")
# bst.dft_print(bst)

# print("\nBreadth-first:")
# bst.bft_print(bst)

# print("\nPre-order:")
# bst.pre_order_dft(bst)

# print("\nPost-order:")
# bst.post_order_dft(bst)
