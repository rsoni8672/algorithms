# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Input: numRows = 5
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
#
# Input: numRows = 1
# Output: [[1]]
from typing import List


class Solution:
    def get_pascal_matrix(self, num_rows):
        if num_rows % 2 == 0:
            num_rows += 1
        output = []
        for index in range(num_rows):
            output.append([0] * num_rows)
        output[0][num_rows // 2] = 1
        return output[0:num_rows]

    def generate(self, numRows: int) -> List[List[int]]:
        p_triangle = []
        p_triangle.append([1])

        for num in range(1, numRows):
            row = [1] * (len(p_triangle[-1])+1)
            for index in range(1, len(row)-1):
                row[index] = p_triangle[-1][index-1]+p_triangle[-1][index]
            p_triangle.append(row)
        return p_triangle

if __name__=="__main__":
    solution = Solution()
    print(solution.generate(5))
    print(solution.generate(4))
    print(solution.generate(1))