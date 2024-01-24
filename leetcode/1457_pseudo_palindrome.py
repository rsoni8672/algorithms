# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self, root, freq_map, output):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            freq_map[root.val] = freq_map.get(root.val, 0) + 1
            print(freq_map)
            isOddNumberFound = False
            for item in freq_map:
                if freq_map[item] % 2 != 0 and isOddNumberFound:
                    freq_map[root.val] = freq_map.get(root.val, 0) - 1
                    if freq_map[root.val] == 0:
                        freq_map.pop(root.val)
                    return 0
                if freq_map[item] % 2 != 0:
                    isOddNumberFound = True
            print("returning 1")
            freq_map[root.val] = freq_map.get(root.val, 0) - 1
            if freq_map[root.val] == 0:
                freq_map.pop(root.val)
            return 1
        freq_map[root.val] = freq_map.get(root.val, 0) + 1
        output = output + self.solve(root.left, freq_map, output) + self.solve(root.right, freq_map, output)
        freq_map[root.val] = freq_map.get(root.val, 0) - 1
        if freq_map[root.val] == 0:
            freq_map.pop(root.val)

        return output

    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        freq_map = {}
        output = 0
        return self.solve(root, freq_map, output)