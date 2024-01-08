class Solution:
    def get_sum(self, root, initial_sum, low, high):
        if root is None:
            return 0
        if root.val > high:
            return 0
        if root.val < low:
            return 0
        return initial_sum + root.val + self.get_sum(root.right, initial_sum, low, high) + self.get_sum(root.right, initial_sum, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        initial_sum = 0
        return self.get_sum(root, initial_sum, low, high)

if __name__=="__main__":
    soln = Solution()
    soln.rangeSumBST()