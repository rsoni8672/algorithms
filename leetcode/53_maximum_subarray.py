from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp_array = [0] * len(nums)
        temp_array[0] = nums[0]
        for index in range(1, len(nums)):
            if nums[index] + temp_array[index - 1] > nums[index]:
                temp_array[index] = nums[index] + temp_array[index - 1]
            else:
                temp_array[index] = nums[index]
        print(temp_array)
        return max(temp_array)


if __name__ == "__main__":
    solution = Solution()
    solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
