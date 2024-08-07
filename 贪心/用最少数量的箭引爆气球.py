from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        temp = points[0]
        for i in range(1, len(points)):
            temp = [points[i][0], min(temp[1],points[i][1])]
            if temp[0] > temp[1]:
                res += 1
                temp = points[i]
        return res