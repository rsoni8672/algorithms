from typing import List


class Solution:
    def temp(self, current_index, nums, doable):
        if current_index >= len(nums):
            doable = True
        elif current_index == len(nums) -1:
            doable = True
        elif nums[current_index] == 0:
            doable = False
        else:
            for index in range(nums[current_index]):
                return self.temp(current_index + index, nums, doable);
        return doable
    def canJump(self, nums: List[int]) -> bool:
        return self.temp(0, nums, False)

if __name__ == "__main__":
    soln = Solution()
    numbers = [2,3,1,1,4]
    print(soln.canJump(numbers))
