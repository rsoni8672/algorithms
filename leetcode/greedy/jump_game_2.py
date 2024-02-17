from typing import List


class Solution:

    def find_minimum_jumps(self, index, nums, cache):
        if index in cache:
            return cache[index]

        if index >= len(nums)-1:
            return 0
        if nums[index] == 0:
            cache[index] = len(nums) + 1
            return cache[index]
        minimum_value = len(nums)
        for jumps in range(nums[index]):
            temp = self.find_minimum_jumps(index + jumps + 1, nums, cache)
            if temp < minimum_value:
                minimum_value = temp
        cache[index] = 1 + minimum_value
        return 1 + minimum_value

    def jump(self, nums: List[int]) -> int:
        cache = {}
        return self.find_minimum_jumps(0, nums, cache)
