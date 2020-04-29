"""
Interview Prep :: Exercises

Add Two Numbers
https://leetcode.com/problems/add-two-numbers/

* You are given two non-empty linked lists representing two positive integers.
* The digits are stored in reversed order, and each of their nodes contain a single digit.
* Add the two numbers and return it as a linked list.
* You may assume the two numbers do not contain any leading zero, except the number 0.

My own example: 1234

* Represented as the linked list: 4 -> 3 -> 2 -> 1
* Sum as we go:

4 -> 3 -> 2 -> 1
9 -> 8 -> 7
Sum: 2,221
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reconstruct_integer(ll: ListNode) -> int:
    # Reconstruct the two integers
    # Iterate through list, with an index counter
    index = 0
    total = 0
    node = ll
    while node:
        # Multiply each value by 10 ** index counter
        digit_amt = node.val * (10 ** index)
        # e.g. 4 * 10 ** 0 = 4 * 1 = 4
        # Add digit amount to total
        total += digit_amt
        # Increment index counter
        index += 1
        # Move to next node
        node = node.next

    return total



def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Reconstruct input lists into integers
    int_1 = reconstruct_integer(l1)
    int_2 = reconstruct_integer(l2)
    # Once reconstructed, sum the two integers
    int_sum = int_1 + int_2
    # Convert result back to linked list
    # Keep track of previous node, to set node.next
    node_list = []
    prev_node = None
    while int_sum > 0:
        # Extract value of last digit
        digit_val = int_sum % 10
        # Instantiate new node and append to list
        node_list.append(ListNode(digit_val))
        if prev_node is not None:
            prev_node.next = node_list[-1]
        # Remove last digit from sum
        int_sum = int_sum // 10
        # Set new node to prev node
        prev_node = node_list[-1]

    # return head node
    if len(node_list) > 0:
        return node_list[0]
    else: # or 0 (in case of 0 input)
        return ListNode(0)


def add_two_nums_str(l1: ListNode, l2: ListNode) -> ListNode:
    # === Naive string conversion method === #
    # Reconstruct the two integers
        # Iterate through both lists
            # Extract value of each node
            # Convert to string, concatenate with previous digits
    # Sum the two integers, convert to string
    # Iterate through digits
        # Convert each one to int and assign as node.val

    # First, convert to string, allowing iteration
    # int_sum_str = str(int_sum)[::-1]
    # Iterate through digits


if __name__ == "__main__":
    four = ListNode(4)
    three = ListNode(3)
    two = ListNode(2)
    one = ListNode(1)
    four.next = three
    three.next = two
    two.next = one

    print(reconstruct_integer(four))

    nine = ListNode(9)
    eight = ListNode(8)
    seven = ListNode(7)
    nine.next = eight
    eight.next = seven

    print(reconstruct_integer(nine))

    print(add_two_numbers(four, nine))


