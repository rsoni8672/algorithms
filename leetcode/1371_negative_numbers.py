from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for row_idx in range(rows):
            for col_idx in range(cols):
                if grid[row_idx][col_idx] < 0:
                    count += cols - col_idx
                    break
        return count


if __name__ == '__main__':
    soln = Solution()
    print(soln.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))