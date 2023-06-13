from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for col_index in range(len(grid)):
                array = [grid[row_index][col_index] for row_index in range(len(grid))]
                if row == array:
                    count += 1

        return count

if __name__=='__main__':
    soln = Solution()
    print(soln.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))