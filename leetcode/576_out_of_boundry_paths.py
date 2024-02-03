class Solution:
    def get_directions(self, current_row, current_column, m, n):
        output = []
        if current_row + 1 < m:
            output.append([current_row+1, current_column])
        if current_row - 1 >= 0:
            output.append([current_row-1, current_column])
        if current_column + 1 < n:
            output.append([current_row, current_column+1])
        if current_column - 1 >= 0:
            output.append([current_row, current_column-1])

        return output

    def get_score(self,m, n, row, col):
        output = 0
        if row == 0:
            output += 1
        if row == m-1:
            output += 1
        if col == 0:
            output += 1
        if col == n-1:
            output += 1
        return output




    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache = {}
        def solve(max_move, start_row, start_column):
            if start_row < 0 or start_row >= m or start_column < 0 or start_column >= n:
                return 1
            if max_move == 0:
                return 0
            if (start_row, start_column, max_move) in cache:
                return cache[(start_row, start_column, max_move)]
            cache[(start_row, start_column, max_move)] = ((solve(max_move-1, start_row+1, start_column) + solve(max_move-1, start_row-1, start_column)) % (10**9+7) +
             (solve(max_move-1, start_row, start_column+1) + solve(max_move-1, start_row, start_column-1))%(10**9+1))%(10**9+7)
            return cache[(start_row, start_column, max_move)]
        return solve(maxMove, startRow, startColumn)

if __name__ == "__main__":
    soln = Solution()
    print(soln.findPaths(2, 2, 2, 0, 0))



