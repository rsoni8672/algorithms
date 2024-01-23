# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMaxDiff(self, root, currentDiff):
        if root is None:
            return 0, 0
        if root.left is None and root.right is None:
            return root.val, root.val

        left_min, left_max = self.getMaxDiff(root.left)
        right_min, right_max = self.getMaxDiff(root.right)

        difference = max(abs(root.val - left_max), abs(root.val - left_min), abs(root.val - right_min), abs(root.val - right_max))

        return max(currentDiff, difference)



    def maxAncestorDiff(self, root: Optional[TreeNode]) -> None:
        return self.getMaxDiff(root, -1)
