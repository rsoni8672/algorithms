from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        freq_map = {}
        for num in nums1:
            freq_map[num] = freq_map.get(num , 0 )+1

        print(freq_map)
        output = []

