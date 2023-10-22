from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output_count = 0
        for i_index in range(len(nums)):
            for j_index in range(i_index + 1, len(nums)):
                if nums[i_index] == nums[j_index]:
                    output_count += 1
        return output_count


if __name__ == '__main__':
    solution = Solution()
    print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
    print(solution.numIdenticalPairs([1, 1, 1, 1]))
    print(solution.numIdenticalPairs([1, 2, 3]))
