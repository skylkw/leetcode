# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.res = 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        if self.dfs(root) == 0:
            self.res += 1

        return self.res

    def dfs(self, cur: Optional[TreeNode]):
        if cur is None:
            return 2
        left = self.dfs(cur.left)
        right = self.dfs(cur.right)

        if left == 2 and right == 2:
            return 0

        if left == 0 or right == 0:
            self.res += 1
            return 1

        if left == 1 or right == 1:
            return 2
