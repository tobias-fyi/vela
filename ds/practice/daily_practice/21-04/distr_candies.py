"""Distribute Candies - LeetCode Problem"""

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Calculate number of candies Alice can eat
        # Find number of unique types of candies
        # Return the lower of the two
        pass


def distributeCandies(candyType: List[int]) -> int:
    # Calculate number of candies Alice can eat
    num_can_eat = int(len(candyType) / 2)
    # Find number of unique types of candies
    num_types = int(len(set(candyType)))
    # Return the lower of the two
    return num_can_eat if num_can_eat < num_types else num_types


# One-liner
def distributeCandiesOneLiner(candyType: List[int]) -> int:
    return (
        int(len(candyType) / 2)
        if int(len(candyType) / 2) < int(len(set(candyType)))
        else int(len(set(candyType)))
    )


if __name__ == "__main__":
    ans_1 = distributeCandies([1, 1, 2, 2, 3, 3])
    print(ans_1)
    assert ans_1 == 3

    ans_2 = distributeCandies([1, 1, 2, 3])
    print(ans_2)
    assert ans_2 == 2

    ans_3 = distributeCandies([6, 6, 6, 6])
    print(ans_3)
    assert ans_3 == 1

    # One-liner version
    ans_1 = distributeCandiesOneLiner([1, 1, 2, 2, 3, 3])
    print(ans_1)
    assert ans_1 == 3

    ans_2 = distributeCandiesOneLiner([1, 1, 2, 3])
    print(ans_2)
    assert ans_2 == 2

    ans_3 = distributeCandiesOneLiner([6, 6, 6, 6])
    print(ans_3)
    assert ans_3 == 1
