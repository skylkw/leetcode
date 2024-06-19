from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        end = 0
        max_end = 0
        step = 0
        for i in range(len(nums)-1):
            max_end = max(max_end,nums[i]+i)
            if i == end:
                end = max_end
                step += 1
        return step