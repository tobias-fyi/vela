"""
Data Structures :: LRU Cache
"""

from doubly_linked_list import DoublyLinkedList


class LRUCache:
    def __init__(self, limit=10):
        """The LRUCache class keeps track of the max number of nodes it
        can hold, the current number of nodes it is holding, a doubly-
        linked list that holds the key-value entries in the correct
        order, as well as a storage dict that provides fast access
        to every node stored in the cache.
        """
        self.limit = limit
        self.order = DoublyLinkedList()
        self.storage = dict()

    def get(self, key):
        """Retrieves the value associated with the given key.
        
        Moves the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        # Key is not in cache - return None
        if key not in self.storage:
            return None
        # Key is in cache
        else:
            # Move to most recently used
            node = self.storage[key]
            self.order.move_to_end(node)
            # Return value
            return node.value[1]

    def set(self, key, value):
        """Adds the given key-value pair to the cache.
        
        The newly-added pair is considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache is removed to make room. In the case that the key
        already exists in the cache, the old value associated with
        the key is overwritten by the new value.
        """
        # If item exists
        if key in self.storage:
            # Overwrite value
            node = self.storage[key]
            node.value = (key, value)
            # Move to tail
            self.order.move_to_end(node)

        # Size is at limit
        if len(self.order) == self.limit:
            # Remove oldest item
            oldest_index = self.order.head.value[0]
            del self.storage[oldest_index]
            self.order.remove_from_head()
            # Add newest to end
        # Size is not at limit
        # Add to order
        self.order.add_to_tail((key, value))
        # Add to storage
        self.storage[key] = self.order.tail


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
