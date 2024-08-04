# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def help(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left_height = help(node.left)
            if left_height == -1:
                return -1
            right_height = help(node.right)
            if right_height == -1 or abs(right_height-left_height) > 1:
                return -1
            return max(left_height,right_height) + 1
        
        return help(root) != -1