from functools import cache


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#         m = len(text1)
#         n = len(text2)

#         @cache
#         def dfs(i, j):
#             if i < 0 or j < 0:
#                 return 0
#             if text1[i] == text2[j]:
#                 return dfs(i - 1, j - 1) + 1

#             return max(dfs(i - 1, j), dfs(i, j - 1))

#         return dfs(m - 1, n - 1)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[m][n]
