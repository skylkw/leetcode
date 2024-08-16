from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        m = len(nums1)
        n = len(nums2)
        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    for k in range(j + 1, n):
                        if nums2[k] > nums1[i]:
                            res[i] = nums2[k]
                            break

        return res
