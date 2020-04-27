"""
Data Structures :: LRU Cache
"""


class CacheNode:
    def __init__(self, key, value, prev=None, next=None):
        """A node in a doubly-linked list-based LRU cache.
        
        :param key              : Key by which to access nodes.
        :param value            : Value accessed by key.
        :param prev [CacheNode] : Previous CacheNode in list, defaults to None
        :param next [CacheNode] : Next CacheNode in list, defaults to None
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


class LRUCache:
    def __init__(self, node=None, limit=10):
        """The LRUCache class keeps track of the max number of nodes it
        can hold, the current number of nodes it is holding, a doubly-
        linked list that holds the key-value entries in the correct
        order, as well as a storage dict that provides fast access
        to every node stored in the cache.

        :param node [CacheNode] : Optional initial CacheNode.
        :param limit [int] : Max number of elements in cache, default 10.
        """
        self.head = node  # Head of cache is most recent
        self.tail = node  # Tail of cache is oldest
        self.limit = limit
        self.length = 1 if node is not None else 0
        # self.storage = DoublyLinkedList()

    def __len__(self):
        """Returns number of elements currently in cache."""
        return self.length

    def move_to_head(self, node):
        """Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        
        :param node (ListNode) : Node to be moved to head.
        """
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def get(self, key):
        """Retrieves the value associated with the given key.
        
        Moves the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        node = self.head
        value = None
        exists = False
        while node:  # Loop through nodes, looking for key
            if node.key == key:
                exists = True
                break

        if exists:
            if node is self.head:
                value = node.value
            else:
                self.delete(node)

        new_node = CacheNode(key, value)
        self.length += 1

        return value

    def set(self, key, value):
        """Adds the given key-value pair to the cache.
        
        The newly-added pair is considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache is removed to make room. In the case that the key
        already exists in the cache, the old value associated with
        the key is overwritten by the new value.
        """
        # First, look for the key in the cache using `self.get()`
        # If not exists (returns None), add key-value to head
        # If exists, pop old key-value from list, add new value to head
        pass

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
