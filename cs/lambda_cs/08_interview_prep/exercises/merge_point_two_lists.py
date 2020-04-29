"""
Interview Preparation :: Day 2 lesson

Live coding through an example from HackerRank:

[Find the Merge Point of Two Linked Lists](http://hr.gs/cfcfac)

Given pointers to the head nodes of 2 linked lists that merge together at some point,
find the Node where the two lists merge.

It is guaranteed that the two head Nodes will be different, and neither will be null.

Complete the method so that it finds and returns the data value of the Node where the
two lists merge.
"""

class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None



def find_merge_node(head1: ListNode, head2: ListNode):
    # === Use a visited set === #
    # Traverse one list, adding nodes to visited
    # Traverse other list, comparing node.next to pointers in set
    # Once there is a match, return that node's value
    curr = head1
    s = set()

    while curr:
        s.add(curr)
        curr = curr.next

    curr = head2

    while curr:
        if curr in is:
            return curr.data
        curr = curr.next


