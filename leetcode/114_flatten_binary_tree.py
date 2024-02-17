from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root, arr):
        if root is None:
            return
        arr.append(root.val)
        print(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        arr = [1, 2, 3, 4, 5, 6]
        # self.dfs(root, arr)
        print("Arr - ", arr)

        if len(arr) > 0:
            head = TreeNode(arr[0])
            root = head
            index = 1
            while index < len(arr):
                print(arr[index])
                index += 1
if __name__ == "__main__":
    solution = Solution()
    solution.flatten(None)


