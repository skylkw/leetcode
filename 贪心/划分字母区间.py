from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_locations = {}
        for i in range(len(s)):
            end_locations[s[i]] = i

        max_end = 0
        start = 0
        res = []
        for i in range(len(s)):
            max_end = max(max_end, end_locations[s[i]])
            if i == max_end:
                res.append(i - start + 1)
                start = max_end + 1
        return res
