# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
#
# You must do it in place.
#
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        column_indexes = set()
        row_indexes = set()

        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if matrix[row][column] == 0:
                    row_indexes.add(row)
                    column_indexes.add(column)

        for row in row_indexes:
            matrix[row] = [0] * len(matrix[0])

        for column in column_indexes:
            for row in matrix:
                row[column] = 0

        print(matrix)


if __name__ == "__main__":
    solution = Solution()
    print(solution.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(solution.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
