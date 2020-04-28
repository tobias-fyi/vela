"""
Interview Prep :: Exercises

Contains Duplicate (LeetCode)
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.

Your function should return True if any value appears at least twice in the array,
and it should return False if every element is distinct.
"""

from __future__ import annotations
from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    """Returns True if array contains 1+ duplicate elements,
    otherwise, it returns False.
    """
    # Convert list into set and compare lengths
    # if length of set is less than that of list,
    # then duplicates exist
    return len(set(nums)) < len(nums)


if __name__ == "__main__":
    num_list = [1, 2, 3, 1]  # Should return True
    # num_list = [1, 2, 3, 5]  # Should return False
    print(contains_duplicate(num_list))

