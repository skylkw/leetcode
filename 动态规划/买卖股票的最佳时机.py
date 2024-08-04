from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         cost = prices[0]
#         for price in prices:
#             cost = min(cost, price)
#             profit = max(price - cost, profit)
#         return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],-prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0] + prices[i])

        return dp[len(prices)-1][1]

