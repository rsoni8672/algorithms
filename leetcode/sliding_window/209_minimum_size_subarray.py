from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_index = 0
        current_sum = 0

        minimum_length = len(nums) + 1
        index = 0
        while index < len(nums):
            current_sum = current_sum + nums[index]
            if current_sum >= target:
                if index - current_index < minimum_length:
                    minimum_length = index - current_index + 1
            elif current_sum > target:
                while current_sum > target:
                    print("in while")
                    current_sum = current_sum - nums[current_index]
                    current_index += 1
                if current_sum >= target:
                    if index - current_index < minimum_length:
                        minimum_length = index - current_index + 1
            index += 1
        return minimum_length


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
