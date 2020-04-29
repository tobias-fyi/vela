# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    # the data on the linked list nodes might not be unique 
    # we can't rely on just checking the data in each node 
    # as with any node-based data structure, each node is a unique 
    # region in memory 
    # the actual data on the merge point node is what we're going to return 

    # why a set? because sets are good at noting what we've seen already 
    # sets are good at holding unique things 
    # the linked lists kept track of the order of elements for us, so that 
    # the set didn't have to 
    # sets on their own do not keep track of the order in which elements 
    # are inserted 

    # Idea 1: if we're opting to not mutate list nodes 
    # Runtime: O(n + m) where n and m are the lengths of the two lists 
    # Space: O(n)
    # we can use a set to keep track of nodes we've visited 
    # traverse one of the lists, adding each node to a visited set 
    # traverse the other list, checking to see if each node is in the set 
    # return the value of the first node in the second list that we find 
    # in the set 
    curr = head1
    s = set()

    while curr:
        s.add(curr)
        curr = curr.next

    curr = head2

    while curr:
        if curr in s:
            return curr.data
        curr = curr.next

    # Idea 2: If we allow mutation of the input 
    # Runtime: O(n + m) where n and m are the lengths of the two lists 
    # Space: O(1)
    # traverse one of the lists, adding an attribute on each node to 
    # signify that we've seen this node before 
    # traverse the other list until we find the first node that has 
    # the attribute 
    # curr = head1
    
    # while curr:
    #     curr.visited = True 
    #     curr = curr.next

    # curr = head2
        
    # while curr:
    #     if hasattr(curr, 'visited'):
    #         return curr.data
    #     curr = curr.next