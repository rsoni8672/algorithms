from typing import List


class Solution:
    def helper(self, start_row, end_row, start_column, end_column, matrix, depth):
        # print("_________________________")
        print(start_row, end_row, start_column, end_column)
        if start_row >= end_row:
            return;
        start_row_arr = []
        for element in matrix[start_row][start_column:end_column+1]:
            start_row_arr.append(element)
        end_row_arr = []
        for element in matrix[end_row][start_column:end_column+1]:
            end_row_arr.append(element)

        start_col_arr = []
        for arr in matrix[start_row:end_row+1]:
            start_col_arr.append(arr[start_column])
        end_col_arr = []
        for arr in matrix[start_row:end_row+1]:
            end_col_arr.append(arr[end_column])

        start_col_arr = start_col_arr[::-1]
        end_col_arr = end_col_arr[::-1]

        # print(start_row_arr, end_row_arr)
        # print(start_col_arr, end_col_arr)

        for index in range(start_column, end_column+1, 1):
            matrix[start_row][index] = start_col_arr[index-depth]

        for index in range(start_column, end_column+1, 1):
            matrix[end_row][index] = end_col_arr[index-depth]

        for index in range(start_row, end_row+1):
            matrix[index][end_column] = start_row_arr[index-depth]

        for index in range(start_row, end_row+1):
            matrix[index][start_column] = end_row_arr[index-depth]

        self.helper(start_row + 1, end_row - 1, start_column + 1, end_column - 1, matrix, depth+1)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.helper(0, len(matrix) - 1, 0, len(matrix) - 1, matrix, 0)


if __name__ == "__main__":
    solution = Solution()
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    solution.rotate(matrix)
