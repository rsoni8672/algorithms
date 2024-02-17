from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        count_map = {}

        for num in freq_map:
            temp = count_map.get(freq_map[num], [])
            temp.append(num)
            count_map[freq_map[num]] = temp

        minimum_frequencies = sorted(count_map.keys())
        print(count_map)

        while k >= 0:
            for freq in minimum_frequencies:
                elements = count_map[freq]
                for element in elements:
                    k = k - freq
                    if k >= 0:
                        freq_map.pop(element)
                    else:
                        break
        print(freq_map)
        return len(freq_map)

if __name__ == "__main__":
    solution = Solution()
    arr = [4,3,1,1,3,3,2]
    k = 3
    print(solution.findLeastNumOfUniqueInts(arr, k))

