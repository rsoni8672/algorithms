from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_queue = []
        negative_queue = []

        for index in range(len(nums)):
            if nums[index] > 0:
                positive_queue.append(nums[index])
            else:
                negative_queue.append(nums[index])

        output_index = 0
        index = 0
        while index < len(positive_queue):
            nums[output_index] = positive_queue[index]
            output_index += 1
            nums[output_index] = negative_queue[index]
            output_index += 1
            index += 1
        return nums
