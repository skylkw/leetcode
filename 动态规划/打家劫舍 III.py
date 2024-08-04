# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            if node is None:
                return 0, 0
            l_1, l_2 = dfs(node.left)
            r_1, r_2 = dfs(node.right)
            rob = l_2 + r_2 + node.val
            rob_not = l_1 + r_1
            return rob, rob_not
        return max(dfs(root))
