from typing import List


class Solution:
    def lcs(self, nums1, nums2):
        dp_array = [[0] * len(nums1) for _ in range(len(nums2))]

        for index1 in range(len(nums2)):
            for index2 in range(len(nums1)):
                if nums1[index1] == nums2[index2]:
                    if index1 == 0 or index2 == 0:
                        dp_array[index1][index2] = 1
                    else:
                        dp_array[index1][index2] = dp_array[max(0, index1 - 1)][max(0, index2 - 1)] + 1
            print(dp_array)
        return max([max(row) for row in dp_array])

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        return self.lcs(nums1, nums2)


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,0,0,0,1]
    nums2 = [1,0,0,1,1]
    print(solution.lcs(nums1, nums2))
