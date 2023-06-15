from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    level_sum_map = {}

    def traverse(root: TreeNode, level):
        if root is not None:
            Solution.level_sum_map[level] = Solution.level_sum_map.get(level, 0) + root.val
            Solution.traverse(root.left, level + 1)
            Solution.traverse(root.right, level + 1)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        Solution.level_sum_map = {}
        Solution.traverse(root, 1)

        max_sum = -111111
        max_level = -1
        for key, val in Solution.level_sum_map.items():
            if val == max_sum:
                if max_level > key:
                    max_level = key
                    max_sum = val

            elif val > max_sum:
                max_level = key
                max_sum = val
        return max_level
