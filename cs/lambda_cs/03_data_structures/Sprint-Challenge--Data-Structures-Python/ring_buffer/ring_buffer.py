

from doubly_linked_list import DoublyLinkedList
from typing import Any


class RingBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item: Any) -> None:
        """Adds an element to the buffer."""
        if len(self.storage) < self.capacity:
            # If buffer is not full, simply add to tail
            self.storage.add_to_tail(item)
            self.current = self.storage.tail  # Update cursor
        else:  # If buffer is full, overwrite next item
            # If cursor is on tail, loop back to head
            if self.current.next is None:
                # Replace head node with new item
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head  # Set cursor to new head
            else:  # If cursor is not at tail, replace next item
                # Uses the ListNode methods (don't update list length)
                self.current.next.delete()  # Remove next item
                # Insert new item after current
                self.current.insert_after(item)
                # Set current to next item
                self.current = self.current.next

    def get(self) -> list:
        """Returns all of the elements in the buffer 
        in a list in their given order.
        """
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # Set initial current node
        node = self.storage.head

        # Iterate through DLL, appending values to list in order
        while node:
            if node.value is not None:
                list_buffer_contents.append(node.value)
            node = node.next

        return list_buffer_contents


# ============ Stretch Goal ============ #
class ArrayRingBuffer:
    def __init__(self, capacity: int):
        """Ring buffer (circular buffer) implemented using a Python list.
        
        The behavior of the ring buffer means that the list always stays
        the same length, and thus overcomes the problem with lists having
        to be reinstantiated whenever they are extended beyond the capacity
        of their current block of memory.
        """
        self.capacity = capacity
        # Instantiate array of length capacity
        self.storage = [None] * capacity
        # Start out at index 0
        self.current = 0

    def append(self, item: Any) -> None:
        """Adds an element to the buffer.
        
        One advantage of the list-based ring buffer is the ease with which
        the items are accessed via their indices.
        """
        # Replace current index with item
        self.storage[self.current] = item
        # Move to next item in list
        if self.current == len(self.storage) - 1:
            # If current is at end of list, start from beginning
            self.current = 0
        else:  # If not at end, increment index counter
            self.current += 1

    def get(self) -> list:
        """Returns all of the elements in the buffer 
        in a list in their given order.

        One of the advantages of the list-based ring buffer is that a new
        list does not have to be created in order to return the items.
        """
        # List comprehension to return only non-None items
        return [item for item in self.storage if item is not None]
