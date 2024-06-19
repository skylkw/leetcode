from typing import List
from utils import TreeSet

# 352. 将数据流变为多个不相交区间


class SummaryRanges:

    def __init__(self):
        self.intervals = TreeSet()

    def addNum(self, value: int) -> None:
        interval = [value, value]
        if interval in self.intervals:
            return
        lower = self.intervals.lower(interval)
        higher = self.intervals.higher(interval)
        if higher and higher[0] == value:
            return
        if lower and lower[1] + 1 == value and higher and higher[0] == value + 1:
            lower[1] = higher[1]
            self.intervals.remove(higher)
        elif lower and lower[1] + 1 >= value:
            lower[1] = max(lower[1], value)
        elif higher and higher[0] == value + 1:
            higher[0] = value
        else:
            self.intervals.add(interval)

    def getIntervals(self) -> List[List[int]]:
        return list(self.intervals)


if __name__ == "__main__":
    ranges = [[], [1], [], [3], [], [7], [], [2], [], [6], []]
    obj = SummaryRanges()
    for r in ranges:
        if r:
            obj.addNum(r[0])
        print(obj.getIntervals())
