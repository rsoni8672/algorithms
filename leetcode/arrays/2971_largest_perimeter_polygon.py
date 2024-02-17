from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        total_sum = sum(nums) - nums[-1]
        index = len(nums) - 1
        # print("Total sum ", total_sum)

        while index > 0:
            if total_sum > nums[index]:
                return total_sum + nums[index]
            total_sum = total_sum - nums[index - 1]
            index -= 1
        return -1


if __name__=="__main__":
    solution = Solution()
    nums = [5,5,50]
    print(solution.largestPerimeter(nums))