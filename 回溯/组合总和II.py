from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        self.dfs(candidates, target, 0, 0, [], res)
        return res

    def dfs(
        self,
        candidates: List[int],
        target: int,
        start: int,
        total: int,
        path: List[int],
        res: List[List[int]],
    ):
        if total > target:
            return
        if total == target:
            res.append(path.copy())
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            num = candidates[i]
            path.append(num)
            total += num
            self.dfs(candidates, target, i + 1, total, path, res)
            path.pop()
            total -= num
