from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_end = 0
        for i in range(n):
            if i > max_end:
                return False
            max_end = max(max_end, nums[i] + i)
            if max_end >= n - 1:
                return True
        return False