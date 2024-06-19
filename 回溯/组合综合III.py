from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.dfs(k, n, 1, 0, [], res)
        return res

    def dfs(
        self,
        k: int,
        n: int,
        start: int,
        total: int,
        path: List[int],
        res: List[List[int]],
    ):
        if total > n:
            return
        if len(path) == k and total == n:
            res.append(path.copy())
            return
        for i in range(start, 10):
            path.append(i)
            total += i
            self.dfs(k, n, i + 1, total, path, res)
            path.pop()
            total -= i
