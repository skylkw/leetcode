from typing import List
from collections import deque


# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         def bfs(gird, i: int, j: int):
#             m = len(grid)
#             n = len(gird[0])
#             directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
#             queue = deque()
#             queue.append([i, j])
#             while queue:
#                 node = queue.pop()
#                 for direction in directions:
#                     next_i, next_j = node[0] + direction[0], node[1] + direction[1]
#                     if (
#                         next_i >= 0
#                         and next_i < m
#                         and next_j >= 0
#                         and next_j < n
#                         and grid[next_i][next_j] == "1"
#                     ):
#                         queue.append([next_i, next_j])
#                         grid[next_i][next_j] = "0"

#         m = len(grid)
#         n = len(grid[0])
#         res = 0

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     bfs(grid,i, j)
#                     res += 1
#         return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(gird: List[List[str]], visited: List[List[bool]], i: int, j: int):
            m = len(grid)
            n = len(gird[0])
            directions = [[-1, 0], [0, -1], [0, 1], [1, 0]]
            queue = deque()
            queue.append([i, j])
            visited[i][j] = True
            while queue:
                node = queue.pop()
                for direction in directions:
                    next_i, next_j = node[0] + direction[0], node[1] + direction[1]
                    if (
                        next_i >= 0
                        and next_i < m
                        and next_j >= 0
                        and next_j < n
                        and grid[next_i][next_j] == "1"
                        and not visited[next_i][next_j]
                    ):
                        queue.append([next_i, next_j])
                        grid[next_i][next_j] = "0"
                        visited[next_i][next_j] = True

        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(grid, visited, i, j)
                    res += 1
        return res
