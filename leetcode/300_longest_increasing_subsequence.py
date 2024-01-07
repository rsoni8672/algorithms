from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        increasing_array = [1] * len(nums)
        for index in range(1, len(nums)):
            left_pointer = index - 1
            min_found = False
            max_len = 0
            while left_pointer >= 0:
                if nums[left_pointer] < nums[index]:
                    if max_len < increasing_array[left_pointer]:
                        max_len = increasing_array[left_pointer]
                left_pointer -= 1
            increasing_array[index] = max_len + 1
            print(increasing_array)
        return max(increasing_array)


if __name__ == "__main__":
    solution = Solution()
    nums = [4,10,4,3,8,9]
    print(solution.lengthOfLIS(nums))
