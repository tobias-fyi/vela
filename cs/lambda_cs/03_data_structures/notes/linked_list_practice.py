"""
Data Structures :: Linked List Practice
"""

# %%
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# %%
# class SinglyLinkedList:
#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node

#     def insert_after(self, value):
#         new_node = Node(value)
#         if not self.head and not self.tail:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node  # Reference to next
#             self.tail = new_node  # Actual value

#     def find_middle_node(self):
#         i = self.head.next
#         j = self.head
#         while i is not None and i.next is not None:
#             i = i.next.next
#             j = j.next


# %%
# Instantantiate list
# the_list = SinglyLinkedList()

# %%
# ============
# Problem #2
# How do you reverse a singly linked list without recursion?
# You may not store the list, or it's values, in another data structure.

# %%
# Apparently variables assigned within while loop are not local scoped
i = 1
while i < 10:
    scoped = 10
    i += 1

# %%
# We need to set up:
# value of current item
# next of current item

# %%
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9


# %%
# Start at head
current = node1
not_first = False
while current.next:
    # store the next node as new current
    new_current = current.next
    # if iteration is second or greater:
    #   set current.next to new next
    new_next = current
    if is_second:
        current.next = new_next
    # if first iteration:
    #   set current.next to null
    else:
        current.next = None
        is_second = True
    # move to new current
    current = new_current

current.next = new_next
