from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        res, left = 0, 0
        n = len(s)
        for right in range(n):
            count[s[right]] += 1
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
            res = max(right - left + 1, res)
        return res
