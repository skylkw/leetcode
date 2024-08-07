from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        s = 0
        res = n + 1
        for right in range(n):
            s += right
            while s >= target:
                res = min(res,right - left + 1)
                s -= nums[left]
                left += 1
        return res if res <= n else 0

