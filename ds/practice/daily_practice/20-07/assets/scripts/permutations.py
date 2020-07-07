from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    # === Base case: nums is length 1 === #
    if len(nums) == 1:
        return nums

    permutations = []

    for i in range(len(nums)):
        nums2 = nums.copy()
        # Freeze up thru index i - i.e. create new list
        frozen = [nums2.pop(i)]
        # Permute recursively on the rest of the numbers
        new_nums = permute(nums2)
        perm = frozen + new_nums
        print(perm)

    return permutations


nums = [1, 2, 3]
permute(nums)
