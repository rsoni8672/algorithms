from typing import List


class Solution:
    def removeKdigits(self, nums: str, k: int):
        monotonic_stack = [nums[0]]
        for index in range(1, len(nums)):
            while k > 0 and len(monotonic_stack) > 0 and monotonic_stack[-1] > nums[index]:
                monotonic_stack = monotonic_stack[:-1]
                k -= 1

            monotonic_stack.append(nums[index])
            if monotonic_stack[-1] == '0' and len(monotonic_stack) == 1:
                monotonic_stack = monotonic_stack[:-1]
        while k > 0 and len(monotonic_stack) > 0:
            monotonic_stack = monotonic_stack[:-1]
            k -= 1

        return ''.join(monotonic_stack) if len(monotonic_stack) > 0 else 0

if __name__ == "__main__":
    solution = Solution()
    nums = "10001"
    k = 4
    print(solution.removeKdigits(nums, k))

