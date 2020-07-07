from __future__ import annotations

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"ListNode({self.val}, {self.next})"


# Helper function to (re)construct linked lists from integers
def int_to_linked_list(num: int, last_node: ListNode = None) -> ListNode:
    """Constructs a linked list from an integer, with digits stored in
    reverse order, each node containing a single digit.
    """
    # === Base case: no more numbers === #
    # But if number starts as 0, should be added as node
    if num == 0 and last_node is not None:
        return None
    # Last digit is first to be added
    # To return last digit, take modulo 10
    last_digit = num % 10
    # Then to remove the last digit, floor divide by 10
    new_num = num // 10
    print(f"{new_num} -> {last_digit}")

    # Create ListNode using last_digit
    node = ListNode(last_digit)
    # Assign to last node's next, if exists
    if last_node:
        last_node.next = node
    # Call function recursively
    int_to_linked_list(new_num, node)
    return node


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Compare values of two nodes
    if l1.val <= l2.val:
        # Instantiate ListNode from lesser value
        first_node = ListNode(l1.val)
        l1 = l1.next
    else:
        first_node = ListNode(l2.val)
        l2 = l2.next

    last_node = first_node
    while l1 or l2:
        if l1 is None:
            node = ListNode(l2.val)
            l2 = l2.next
        elif l2 is None:
            node = ListNode(l1.val)
            l1 = l1.next
        else:
            # Compare values of two nodes
            if l1.val <= l2.val:
                # Instantiate ListNode from lesser value
                node = ListNode(l1.val)
                # Increment pointer for that list
                l1 = l1.next
            else:
                # Instantiate ListNode from lesser value
                node = ListNode(l2.val)
                # Increment pointer for that list
                l2 = l2.next

        # Set last node's next to current node
        last_node.next = node
        last_node = node

    # Return the first node
    return first_node


# === Test it out === #
# Create linked lists
list1 = int_to_linked_list(421)
print(list1)
list2 = int_to_linked_list(431)
print(list2)

# === Merge! === #
list3 = mergeTwoLists(list1, list2)
print(list3)
