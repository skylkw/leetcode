from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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
            if i > 0 and nums[i] == nums[i - 1] or used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.dfs(nums, n, used, path, res)
            path.pop()
            used[i] = False
