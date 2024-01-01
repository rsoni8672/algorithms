from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        output = 0
        consumed = [0]*len(s)
        for greed in g:
            for index in range(len(s)):
                if consumed[index] == 0:
                    if s[index] >= greed:
                        consumed[index] = 1
                        output += 1
                        break
        return output


if __name__ == "__main__":
    runner = Solution()
    greed_factor = [1,2,3]
    cookies = [1,1]
    print(runner.findContentChildren(greed_factor, cookies))