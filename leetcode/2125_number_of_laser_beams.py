from typing import List


class Solution:
    def get_frequency_array(self, bank):
        devices_freq = []
        for row in bank:
            freq = 0
            # print(row.split(''))
            for element in row:
                if element == "1":
                    freq += 1
            if freq > 0:
                devices_freq.append(freq)
        return devices_freq

    def numberOfBeams(self, bank: List[str]) -> int:
        output = 0
        devices_freq = self.get_frequency_array(bank)
        print(devices_freq)
        for index in range(0, len(devices_freq)-1):
            output += devices_freq[index]*devices_freq[index+1]
        return output

if __name__ == "__main__":
    solution = Solution()
    bank = ["000","111","000"]
    print(solution.numberOfBeams(bank))