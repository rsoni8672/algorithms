from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        output = []
        nums.sort()
        print(nums)

        for index in range(0, len(nums)-3, 3):
            if nums[index+2] - nums[index] > k:
                return []
            output.append([nums[index:index+3]])
        return output


if __name__ == "__main__":
    soln = Solution()
    nums = [15, 13, 12, 13, 12, 14, 12, 2, 3, 13, 12, 14, 14, 13, 5, 12, 12, 2, 13, 2, 2]
    k = 2
    print(soln.divideArray(nums, k))
