# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
     

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def help(node: Optional[TreeNode], height):
            if node is None:
                return
            if len(res) == height:
                res.append(node.val)
            help(node.right, height + 1)
            help(node.left, height + 1)

        help(root,0)
        return res
