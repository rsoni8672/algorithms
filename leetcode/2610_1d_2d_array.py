from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums_freq = {}

        for num in nums:
            nums_freq[num] = nums_freq.get(num, 0) + 1

        for num in nums_freq:
            freq = nums_freq[num]
            for op in output:
                if freq == 0:
                    break
                op.append(num)
                freq -= 1
            while freq > 0:
                output.append([num])
                freq -= 1
        return output

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4]
    print(solution.findMatrix(nums))