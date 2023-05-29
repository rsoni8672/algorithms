
from collections import deque



def shortest_bridge(grid):
    visited = []
    def get_directions(r, c):
        return [[r, c + 1], [r, c - 1], [r + 1, c], [r - 1, c]]

    def in_bounds(r, c):
        return not (r < 0 or c < 0 or r >= N or c >= N)

    def dfs(grid, r, c):
        if (not in_bounds(r, c)) or not grid[r][c] == 1 or (r, c) in visited:
            return
        visited.append((r, c))
        for dr, dc in get_directions(r, c):
            dfs(grid, dr, dc)

    def bfs(grid, visited):
        res = 0
        queue = []
        for item in visited:
            queue.append(item)
        while (len(queue) > 0):
            print("QUEUE - ", queue)
            length = len(queue)
            for index in range(length):
                r, c = queue[0]
                queue = queue[1:]
                for dr, dc in get_directions(r, c):
                    if (not in_bounds(dr, dc)) or (dr, dc) in visited:
                        continue
                    if grid[dr][dc] == 1:
                        return res
                    queue.append((dr, dc))
                    visited.append((dr, dc))
            res += 1

    N = len(grid)
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == 1:
                dfs(grid, row, column)
                return bfs(grid, visited)

if __name__ == '__main__':
    print("output - ", shortest_bridge([[0,1],[1,0]]))