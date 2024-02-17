from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        row_start = 0
        row_end = len(matrix[0])

        col_start = 0
        col_end = len(matrix)

        while True:
            for index in range(row_start, row_end):
                output.append(matrix[col_start][index])

            for index in range(col_start + 1, col_end):
                output.append(matrix[index][row_end - 1])

            if col_start + 1 < col_end:
                for index in range(row_end - 2, row_start - 1, -1):
                    output.append(matrix[col_end - 1][index])

            if row_start + 1 < row_end:
                for index in range(col_end - 2, col_start, -1):
                    output.append(matrix[index][row_start])

            col_start += 1
            col_end -= 1
            row_start += 1
            row_end -= 1

if __name__ == "__main__":
    solution = Solution()
    print("OUTPUT ", solution.spiralOrder([[7, 8, 9]]))
