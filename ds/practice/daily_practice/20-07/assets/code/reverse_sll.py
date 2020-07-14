"""
HackerRank :: Reverse a singly-linked list
https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

Complete the reverse function below.

For your reference:

SinglyLinkedListNode:
    int data
    SinglyLinkedListNode next
"""


def reverse(head):
    # head node value can be null
    # Keep track of previous node
    prev_node = None
    cur_node = head
    # Loop through - while node.next
    while cur_node:
        # Save node for overwriting cur_node
        next_node = cur_node.next
        # Set current node's next to prev_node
        cur_node.next = prev_node
        # Pass previous node to next iteration
        prev_node = cur_node
        cur_node = next_node

    return prev_node
