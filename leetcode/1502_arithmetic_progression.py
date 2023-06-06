from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        difference =arr[1] - arr[0]

        for index in range(1, len(arr)):
            if arr[index] - arr[index-1] != difference:
                return False
        return True