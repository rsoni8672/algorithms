from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq_map = {}

        operations: int = 0

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        for num in freq_map:
            if freq_map[num] == 1:
                return -1
            elif freq_map[num]%3 == 0:
                operations += freq_map[num]//3
            else:
                operations += freq_map[num]//3
                operations += 1
        return operations

if __name__ == "__main__":
     solution = Solution()
     input_arr = [2,1,2,2,3,3]
     print(solution.minOperations(input_arr))