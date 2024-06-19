from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        res = []
        self.dfs(nums, n, used, [], res)
        return res

    def dfs(
        self,
        nums: List[int],
        n: int,
        used: List[bool],
        path: List[int],
        res: List[List[int]],
    ):
        if len(path) == n:
            res.append(path.copy())
            return
        for i in range(0, n):
            if not used[i]:
                path.append(nums[i])
                used[i] = True
                self.dfs(nums, n, used, path, res)
                path.pop()
                used[i] = False
