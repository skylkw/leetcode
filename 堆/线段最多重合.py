import heapq

n = int(input())
lines = [list(map(int, input().split())) for i in range(n)]


def max_cover(lines: list[list[int]]):
    min_heap = []
    lines.sort()
    res = 1
    heapq.heappush(min_heap, lines[0][1])
    for i in range(1, len(lines)):
        while len(min_heap) > 0 and min_heap[0] <= lines[i][0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap,lines[i][1])
        res = max(res, len(min_heap))
    print(res)

max_cover(lines)