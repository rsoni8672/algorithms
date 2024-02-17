from typing import List
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        output = [1]*len(nums)
        came_from = [-1]*len(nums)

        output[0] = 1

        for index in range(1, len(sorted_nums)):
            j_index = index - 1
            max_length = -1
            last_index = -1
            while j_index >= 0:
                if sorted_nums[index] % sorted_nums[j_index] == 0:
                    if output[j_index] > max_length:
                        max_length = output[j_index]
                        last_index = j_index
                j_index -= 1
            if max_length != -1:
                output[index] = max_length + 1
                came_from[index] = last_index
            else:
                output[index] = 1
                came_from[index] = -1

        max_index = -1
        max_val = 0
        for index in range(len(output)):
            if max_val <= output[index]:
                max_val = output[index]
                max_index = index

        answer = []

        while max_index >= 0:
            answer.append(sorted_nums[max_index])
            max_index = came_from[max_index]
        return answer

        # print("Answer - ", answer)
        return answer


if __name__ == "__main__":
    solution = Solution()
    # nums = [5,9,18,54,90,108,180,360,540,720]
    nums = [2, 3, 4, 8, 9]
    print(solution.largestDivisibleSubset(nums))
