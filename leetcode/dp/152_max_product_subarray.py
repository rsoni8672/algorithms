from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        running_product = [0]*len(nums)

        current_product = 1
        for index in range(len(nums)):
            if nums[index] == 0:
                current_product = 1
            else:
                current_product = current_product*nums[index]
                running_product[index] = current_product
        print(current_product)
        max_product = nums[0]
        for index1 in range(len(nums)):
            temp = 1
            for index2 in range(index1, len(nums)):
                temp *= nums[index2]
                max_product = max(max_product, temp)
        return max_product









if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([-2,-5,-3]))
