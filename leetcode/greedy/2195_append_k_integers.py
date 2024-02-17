from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums_set = set(nums)
        nums = list(nums_set)
        nums.sort()

        output = (k * (k + 1)) // 2
        current_count = k
        index = 0

        while index < len(nums) and nums[index] <= k:
            print(f"REMOVING - {nums[index]}")
            output -= nums[index]
            current_count -= 1
            index += 1

        print(output)
        nums = set(nums)

        next_num = k + 1
        while current_count < k:
            if next_num not in nums:
                output += next_num
                current_count += 1
            next_num += 1
        return output


if __name__ == "__main__":
    solution = Solution()
    nums = [5, 6]
    k = 6
    print(solution.minimalKSum(nums, k))
