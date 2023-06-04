import math
from typing import List


class Solution:
    def is_neighbour(bomb1, bomb2):
        r1 = bomb1[2]
        r2 = bomb2[2]
        d = (bomb1[0] - bomb2[0]) ** 2 + (bomb1[1] - bomb2[1]) ** 2
        return r1**2 >= d or r2**2 >=d


    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        queue = [tuple(bombs[0])]
        visited = [0] * len(bombs)
        visited[0] = 1

        max_detonation = []
        count = 1
        while len(queue) > 0:
            element = queue[0]
            queue = queue[1:]

            for index in range(len(bombs)):
                bomb = bombs[index]
                if visited[index] == 0:
                    if Solution.is_neighbour(element, tuple(bomb)):
                        queue.insert(0, tuple(bomb))
                        visited[index] = 1
                        count += 1
            if len(queue) == 0:
                max_detonation.append(count)
                count = 1
                for index in range(len(visited)):
                    if visited[index] == 0:
                        queue.insert(0, tuple(bombs[index]))
                        visited[index] = 1
                        break
        if len(max_detonation) == 0:
            return count
        return max(max_detonation)

if __name__ == '__main__':
    soln = Solution()
    print("output - ", soln.maximumDetonation(
        [[855, 82, 158], [17, 719, 430], [90, 756, 164], [376, 17, 340], [691, 636, 152], [565, 776, 5],
         [464, 154, 271], [53, 361, 162], [278, 609, 82], [202, 927, 219], [542, 865, 377], [330, 402, 270],
         [720, 199, 10], [986, 697, 443], [471, 296, 69], [393, 81, 404], [127, 405, 177]]
    ))