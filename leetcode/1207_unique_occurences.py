from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_map = {}
        for number in arr:
            freq_map[number] = freq_map.get(number, 0) + 1

        return len(freq_map.values()) == len(set(freq_map.values()))
