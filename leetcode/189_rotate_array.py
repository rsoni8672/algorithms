from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        rotated_array = [-1]*len(nums)

        for index in range(len(nums) - k):
            rotated_array.append(nums[index])

        print(rotated_array)

        for index in range(k):
            rotated_array.insert(0, nums[len(nums)-index-1])

        for index in range(len(rotated_array)):
            nums[index] = rotated_array[index]