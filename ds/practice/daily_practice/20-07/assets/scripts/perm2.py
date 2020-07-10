# === Not my solution === #
# def permute(nums):
#     if not nums:
#         yield []
#     yield from (
#         [nums[i], *p] for i in range(len(nums)) for p in permute(nums[:i] + nums[i + 1 :])
#     )

from typing import List


# def permute(nums: List[int]) -> List[List[int]]:
#     if not nums:
#         yield []
#     for i in range(len(nums)):
#         for p in permute(nums[:i] + nums[i + 1 :]):
#             yield [nums[i], *p]


def permute(nums: List[int]) -> List[List[int]]:
    if nums is None:
        return []
    permutations = []
    for i in range(len(nums)):
        rem = nums[:i] + nums[i + 1 :]
        perm = permute(rem)
        for n in perm:
            new_perm = [nums[i], *n]
            permutations.append(new_perm)
    return permutations


nums = [1, 2, 3]
print(permute(nums))
