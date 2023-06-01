from typing import List


def shortestPathBinaryMatrix( grid: List[List[int]]) -> int:
    n = len(grid)

    queue = []
    visited = set()

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

    queue.append((0, 0, 1))
    visited.add((0,0))

    while len(queue) > 0:
        element = queue[0]
        queue = queue[1:]
        row, col, length = element
        if min(row, col) < 0 or max(row, col) >= n or grid[row][col] == 1:
            continue
        if row == n - 1 and col == n-1:
            return length
        for dr, dc in directions:
            if (row+dr, col+dc) not in visited:
                visited.add((row+dr, col+dc))
                queue.append((row+dr, col+dc, length+1))
    print(visited)
    return -1


            
if __name__ == '__main__':
    print("output - ", shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))

