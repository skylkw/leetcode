# Definition for a binary tree node.
from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []
        if root is None:
            return res

        queue = deque()
        queue.append(root)

        while queue:
            size = len(queue)
            temp: List[int] = []
            for _ in range(size):

                node: TreeNode = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)

        return res
