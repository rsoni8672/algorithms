from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        output = []
        left_sum = 0
        right_sum = 0

        initial_sum = nums[k]
        if 2*k < len(nums):
            for index in range(k):
                initial_sum += nums[index+k + 1]
                initial_sum += nums[k-index]
            print("Initial sum", initial_sum)

        for index in range(k):
            left_sum+=nums[index]
        for index in range(k, 2*k):
            right_sum+=nums[index]
        output.append((left_sum+right_sum)/2*k +1)
        if 2*k < len(nums):
            for index in range(k, len(nums) - k):
                left_sum -= nums[index - k]
                right_sum += nums
            return output
        return [-1]