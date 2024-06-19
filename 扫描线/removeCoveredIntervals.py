from typing import List

# 1288. 删除被覆盖区间
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        prev_end = 0
        for _, end in intervals:
            if end > prev_end:
                prev_end = end
                count += 1
        return count


if __name__ == "__main__":
    count = Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]])  # 2
    print(count)
