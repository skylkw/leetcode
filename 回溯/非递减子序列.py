from typing import Dict, List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(
        self,
        nums: List[int],
        start: int,
        path: List[int],
        res: List[List[int]],
    ):
        used = {}
        for i in range(start, len(nums)):
            if path and nums[i] <path[-1] or used.get(nums[i]):
                continue
            path.append(nums[i])
            used[nums[i]] = True
            if len(path) > 1:
                res.append(path.copy())
            self.dfs(nums, i + 1, path, res)
            path.pop()
