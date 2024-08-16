from functools import cache, lru_cache
from typing import List


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         target += sum(nums)
#         if target < 0 or target % 2 != 0:
#             return 0

#         m = target // 2
#         n = len(nums)
#         dp = [[0] * (m+1) for _ in range(n+1)]
#         dp[0][0] = 1
#         for i,num in enumerate(nums):
#            for j in range(m+1):
#                if j < num:
#                    dp[i+1][j] = dp[i][j]
#                else:
#                    dp[i+1][j] = dp[i][j-num] + dp[i][j]
#         return dp[n][m]


# class Solution:
#     def findTargetSumWays(self, nums: List[int], target: int) -> int:
#         target += sum(nums)
#         if target < 0 or target % 2 == 1:
#             return 0
#         target = target // 2

#         @cache
#         def dfs(i, s):
#             if i < 0:
#                 return 0 if s != 0 else 1
#             if nums[i] > s:
#                 return dfs(i - 1, s)
#             else:
#                 return dfs(i - 1, s) + dfs(i - 1, s - nums[i])

#         return dfs(len(nums) - 1, target)


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        target += sum(nums)
        if target < 0 or target % 2 == 1:
            return 0
        target = target // 2
        self.res = 0
        n = len(nums)

        @cache
        def dfs(start, target, n):
            if target <= 0:
                if target ==
                self.res += 1
                return
            for i in range(start, n):
                target -= nums[i]
                dfs(i + 1, target, n)
                target += nums[i]

        dfs(0, target, n)

        return self.res
