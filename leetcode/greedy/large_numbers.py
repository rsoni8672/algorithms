from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_str = [str(num) for num in nums]
        nums_str.sort()
        return ('').join(nums_str)
