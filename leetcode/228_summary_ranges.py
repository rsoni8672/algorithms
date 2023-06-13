from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        start_range = 0
        end_range = 0

        for index in range(len(nums)-1):
            if nums[index+1] - nums[index] > 1:
                if start_range == end_range:
                    output.append(str(nums[start_range]))
                else:
                    output.append(str(nums[start_range])+"->"+ str(nums[end_range]))
                end_range += 1
                start_range = end_range
            else:
                end_range += 1
            if index == len(nums) - 2:
                if start_range == end_range:
                    output.append(str(nums[start_range]))
                else:
                    output.append(str(nums[start_range])+"->"+ str(nums[end_range]))

        # if output[-1][-1] != str(nums[-1]):
        #     output.append(str(nums[-1]))
        return output
if __name__ == '__main__':
    solution = Solution()
    print(solution.summaryRanges([0,1,2,4,5,7]))