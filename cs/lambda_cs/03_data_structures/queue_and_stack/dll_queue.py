"""
Data Structures :: Queue
"""

import sys

sys.path.append("../doubly_linked_list")
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        """Implementation of a Queue (FIFO). A doubly-linked list is
        used as the underlying data structure because the methods for
        manipulating the two data structures are very similar."""
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        """Adds an item to the back of the queue.

        :param value : Item to be added to the queue.
        """
        self.storage.add_to_tail(value)

    def dequeue(self):
        """Removes an item from the front of the queue.
        
        :return value : Value of dequeued item or None.
        """
        # Empty queue case is handled by DLL method
        value = self.storage.remove_from_head()
        return value

    def len(self):
        """Calls `len()` on the queue.
        
        :return length (int) : Length of queue.
        """
        return len(self.storage)
