from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    # === Base case: nums is length 1 === #
    if len(nums) == 1:
        return [nums]

    permutations = []

    for i, v in enumerate(nums):
        for perm in permute(nums[:i] + nums[i + 1 :]):
            permutations.append([v] + perm)

    return permutations


nums = [1, 2, 3]
permute(nums)
