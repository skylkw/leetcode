from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums: List[int], start: int, path: List[int], res: List[List[int]]):
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            res.append(path.copy())
            self.dfs(nums, i + 1, path, res)
            path.pop()
