from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            row_set = set()
            for col in row:
                if col in row_set:
                    return False
                if col != ".":
                    row_set.add(col)

        print("HERE")

        # for col_idx in range(len(board[0])):
        #     col_set = set()
        #     for row in board:
        #         if row[col_idx] in col_set:
        #             return False
        #         else:
        #             if row[col_idx] != ".":
        #                 col_set.add(row[col_idx])

        for r_buffer in range(3):
            for row in range(3 * r_buffer, 3 * r_buffer + 3, 1):
                box_set = set()
                for buffer in range(3):
                    for col_index in range(3 * buffer, 3 * buffer + 3, 1):
                        if board[row][col_index] in box_set:
                            return False
                        if board[row][col_index] != '.':
                            box_set.add(board[row][col_index])
                print(box_set)
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))