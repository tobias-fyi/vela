"""
Data Structures :: LRU Cache
"""


class ListNode:
    def __init__(self, key, value, prev=None, next=None):
        """A node in a doubly-linked list-based LRU cache.
        
        :param key              : Key by which to access nodes.
        :param value            : Value accessed by key.
        :param prev [ListNode] : Previous ListNode in list, defaults to None
        :param next [ListNode] : Next ListNode in list, defaults to None
        """
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

    def delete(self):
        """Rearranges the node's previous and next pointers
        accordingly, effectively deleting it."""
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    def __init__(self, node=None):
        """Doubly-linked list class that holds references to
        the list's head and tail nodes, and list length."""
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        """Returns length of list; for use with the built-in
        `len()` function."""
        return self.length

    def add_to_head(self, key, value):
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list."""
        new_node = ListNode(key, value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_tail(self):
        """Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        
        :return value : Value of the removed Node or None.
        """
        if self.tail is not None:
            self.delete(self.tail)

    def move_to_head(self, node):
        """Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        
        :param node (ListNode) : Node to be moved to head.
        """
        if node is self.head:
            return
        key, value = node.key, node.value
        self.delete(node)
        self.add_to_head(key, value)

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail.
        
        :param node (ListNode) : Node to be removed from list.
        """
        # TODO: Catch errors if empty or node not in list
        self.length -= 1  # Update length
        # If head and tail, both get set to None
        if self.head is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:  # If head, set current head to next
            self.head = self.head.next
            node.delete()
        elif node is self.tail:  # If tail, set current tail to prev
            self.tail = self.tail.prev
            node.delete()
        else:  # If regular node, just delete
            node.delete()


class LRUCache:
    def __init__(self, limit=10):
        """The LRUCache class keeps track of the max number of nodes it
        can hold, the current number of nodes it is holding, a doubly-
        linked list that holds the key-value entries in the correct
        order, as well as a storage dict that provides fast access
        to every node stored in the cache.

        Head node is most recent. Tail node is oldest.

        :param node [ListNode] : Optional initial ListNode.
        :param limit [int] : Max number of elements in cache, default 10.
        """
        self.limit = limit
        self.storage = DoublyLinkedList()

    def get(self, key):
        """Retrieves the value associated with the given key.
        
        Moves the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        if len(self.storage) < 1:  # In case nothing in cache
            return None
        node = self.storage.head  # Start at the head
        while node:  # Loop through nodes, looking for key
            if node.key == key:
                value = node.value  # Return value of node
                if node is not self.storage.head:  # If head, no need to move
                    self.storage.move_to_head(node)
                return value  # Returning value implies breaking loop
            node = node.next  # Iterate

    def set(self, key, value):
        """Adds the given key-value pair to the cache.
        
        The newly-added pair is considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache is removed to make room. In the case that the key
        already exists in the cache, the old value associated with
        the key is overwritten by the new value.
        """
        # Look for key in cache using `self.get()`
        if self.get(key) is not None:
            # If exists, the call will relocate it to head position
            # Thus, head will only need to be updated with new value
            # Length of list does not change; does not need checking
            self.storage.head.value = value
        else:
            # If not exists (returns None), add key-value to head
            # Before adding, check length of list
            # If length == limit, remove from tail first
            if len(self.storage) == self.limit:
                self.storage.remove_from_tail()
            self.storage.add_to_head(key, value)


# cache = LRUCache(3)
# cache.set("item1", "a")
# cache.set("item2", "b")
# cache.set("item3", "c")

# cache.set("item2", "z")


# cache.set("item1", "a")
# cache.set("item2", "b")
# cache.set("item3", "c")

# cache.get("item1")
# cache.set("item4", "d")

# cache.get("item1")
# cache.get("item3")
# cache.get("item4")
# cache.get("item2")
