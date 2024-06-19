from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res = 1
        flag = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if flag != 1:
                    res += 1
                    flag = 1
            if nums[i] < nums[i - 1]:
                if flag != -1:
                    res += 1
                    flag = -1
        return res
