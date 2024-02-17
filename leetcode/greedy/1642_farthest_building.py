import heapq
from typing import List


class Solution:
    def solve(self, heights, bricks, ladders, index, cache):
        if index == len(heights) - 1:
            if ladders > 0:
                return 1
            elif heights[index] - heights[index - 1] <= bricks:
                return 1
            return 0
        if bricks < 0 and ladders < 0:
            return 0
        if (index, ladders, bricks) in cache:
            return cache[(index,ladders, bricks)]
        if heights[index] - heights[index - 1] <= 0:
            temp = 1 + self.solve(heights, bricks, ladders, index + 1, cache)
            cache[(index, ladders, bricks)] = temp
            return temp

        elif heights[index] - heights[index - 1] <= bricks:
            if ladders > 0:
                temp = 1 + max(self.solve(heights, bricks - (heights[index] - heights[index - 1]), ladders, index + 1, cache),
                               self.solve(heights, bricks, ladders - 1, index + 1, cache))
                cache[(index, ladders, bricks)] = temp
                return temp
            else:
                temp = 1 + self.solve(heights, bricks - (heights[index] - heights[index - 1]), ladders, index + 1,cache)
                cache[(index, ladders, bricks)] = temp
                return temp
        else:
            if ladders > 0:
                cache[(index, ladders, bricks)] = 1 + self.solve(heights, bricks, ladders - 1, index + 1, cache)
                return cache[(index, ladders, bricks)]
            return 0

    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int):
        maxHeap = []
        count = 0

        for index in range(len(heights)-1):
            if heights[index+1] - heights[index] <= 0:
                count += 1
                continue
            bricks -= (heights[index+1]-heights[index])
            heapq.heappush(maxHeap, heights[index]-heights[index+1])

            if bricks < 0:
                element = heapq.heappop(maxHeap)
                bricks += -element
                ladders -= 1
                if ladders < 0:
                    return index
        return len(heights) - 1
if __name__ == "__main__":
    solution = Solution()
    heights = [1,5,1,2,3,4,10000]
    bricks = 4
    ladders = 1
    print(solution.furthestBuilding(heights, bricks, ladders))
