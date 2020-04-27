"""
Data Structures :: Doubly-linked list
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        """Each ListNode holds a value, a reference to its previous node
        as well as its next node in the List."""
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is point to."""
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        """Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is point to."""
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode."""
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
        `len()` function.
        
        :return (int) : Number of items currently held in list.
        """
        return self.length

    def add_to_head(self, value):
        """Wraps the given value in a ListNode and inserts it
        as the new head of the list.
        
        :param value : Item to be added as new head of list.
        """
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next node the new head of the List.

        :return value : Value of the removed Node or None.
        """
        # In case no item exists to remove, return None
        value = None
        if self.head is not None:
            value = self.head.value
            self.delete(self.head)
        return value

    def add_to_tail(self, value):
        """Wraps the given value in a ListNode and inserts it 
        as the new tail of the list.
        
        :param value : Item to be added as new head of list.
        """
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_tail(self):
        """Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node.
        
        :return value : Value of the removed Node or None.
        """
        # In case no item exists to remove, return None
        value = None
        if self.tail is not None:
            value = self.tail.value
            self.delete(self.tail)
        return value

    def move_to_front(self, node):
        """Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List.
        
        :param node (ListNode) : Node to be moved to head.
        """
        if node is self.head:
            return
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        """Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List.
        
        :param node (ListNode) : Node to be moved to tail.
        """
        if node is self.tail:
            return
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

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

    def get_max(self):
        """Returns the highest value currently in the list.
        
        :return max_value (int) : Maximum value in list.
        """
        # Loop through all nodes looking for the highest value
        # TODO: Handle exceptions
        if not self.head:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
