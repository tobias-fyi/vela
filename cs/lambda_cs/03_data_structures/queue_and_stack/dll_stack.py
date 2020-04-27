"""
Data Structures :: Stack
"""

import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Stack:
    def __init__(self):
        """Implementation of a Stack (LIFO). A doubly-linked list is
        used as the underlying data structure because the methods for
        manipulating the two data structures are very similar."""
        self.storage = DoublyLinkedList()

    def push(self, value):
        """Pushes a new item onto the top (tail) of a stack.
        
        :param value : Value to be added to stack.
        """
        # "Top" of stack is the tail
        self.storage.add_to_tail(value)

    def pop(self):
        """Removes an item from the top (tail) of the queue.
        
        :return value : Value of dequeued item or None.
        """
        # Empty stack case is handled by DLL method
        value = self.storage.remove_from_tail()
        return value

    def len(self):
        """Calls `len()` on the stack.
        
        :return length (int) : Length of stack.
        """
        return len(self.storage)
