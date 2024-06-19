from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = 0
        res = -100000
        for num in nums:
            current = max(num, current + num)
            res = max(res, current)
        return res

# from typing import List


# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         dp = [0] * len(nums)
#         dp[0] = nums[0]
#         res = dp[0]

#         for i in range(1,len(nums)):
#             if dp[i-1]<=0:
#                 dp[i] = nums[i]
#             else:
#                 dp[i] = dp[i-1] + nums[i]
#             res = max(dp[i],res)
#         return res
             