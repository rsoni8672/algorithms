# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
from typing import List


class Solution:
    def sortColors(self, arr: List[int]) -> None:
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
            print(arr)

if __name__ == "__main__":
    solution = Solution()
    solution.sortColors([2,0,2,0,1])
    # solution.sortColors([2,0,1])
