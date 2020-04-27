"""
Data Structures :: Sprint Challenge

Recursive reversal of singly-linked list.
"""


class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        """Singly-linked list only holds reference
        to the head of the list."""
        self.head = None

    def add_to_head(self, value):
        """Adds a new node to the list, at the head."""
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        """Searches the list for a value. Returns True if found."""
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        """Reverses the list, recursively."""
        if node is None:  # Base case
            # No next node means the new head has been found
            return None
        else:  # Recursive case
            self.head = node
            # Get and save the original next node
            next_node = node.get_next()
            # Set the current next to previous
            node.set_next(prev)
            # Pass in original next node as node and current node as previous
            self.reverse_list(next_node, node)


# To test it out while writing reverse_list()
lst = LinkedList()
lst.add_to_head(1)
lst.add_to_head(2)
lst.add_to_head(1)
lst.add_to_head(2)
lst.add_to_head(10)

# Print original list
node = lst.head
while node:
    print(node.value)
    node = node.next_node

# Reverse the list
lst.reverse_list(lst.head, None)
print()

# Print the reversed list
node = lst.head
while node:
    print(node.get_value())
    node = node.get_next()
