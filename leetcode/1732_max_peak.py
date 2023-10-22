from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        current_gain = 0

        for num in gain:
            current_gain += num
            if current_gain > max_altitude:
                max_altitude = current_gain
        return max_altitude
