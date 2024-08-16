from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(n: int, k: int, start: int, path: List[int], res: List[List[int]]):
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(start, n+1):
                path.append(i)
                dfs(n, k, i + 1, path, res)
                path.pop()

        dfs(n, k, 1, [], res)
        return res
