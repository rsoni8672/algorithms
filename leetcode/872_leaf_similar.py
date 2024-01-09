from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_sequence(self, root):
        if root is None:
            return ''
        if root.left is None and root.right is None:
            return str(root.val) + "-" + self.get_sequence(root.left) + "-" + self.get_sequence(root.right)
        return self.get_sequence(root.left) + self.get_sequence(root.right)

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        leaf1_seq = self.get_sequence(root1)
        leaf2_seq = self.get_sequence(root2)
        print(leaf1_seq, leaf2_seq)

        return leaf1_seq == leaf2_seq
