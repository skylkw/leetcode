# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        deepth = 1
        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            for _ in range(size):
                node: TreeNode = queue.popleft()
                if node.left is None and node.right is None:
                    return deepth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            deepth += 1
        return deepth
