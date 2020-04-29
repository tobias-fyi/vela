"""
Interview Practice :: Exercises

LeetCode: Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a
specific target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.
"""

from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    # === Brute force method === #
    # Loop through list
    # Compare value at each index to value at all other indices
    for i1, val1 in enumerate(nums):
        print(f"i1: {i1}, val1: {val1}")
        for i2, val2 in enumerate(nums):
            print(f"i2: {i2}, val2: {val2}")
            if i2 == i1:
                continue
            if val1 + val2 == target:
                return [i1, i2]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]

    print(two_sum(nums, 9))

