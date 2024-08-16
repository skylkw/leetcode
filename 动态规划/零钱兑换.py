from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(i,c):
            if i < 0:
                return 0
            if coins[i] > c:
                return dfs(i-1,c)
            return min(dfs(i,c-coins[i])+coins[i] ,dfs(i-1,c))
        return dfs(len(coins) -1,amount)