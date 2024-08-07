from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:

        max_left = nums[0]
        left = 0
        for i in range(1,len(nums) - 1):
            if nums[i] < max_left:
                left = i
            else:
                max_left = nums[i]
        return left