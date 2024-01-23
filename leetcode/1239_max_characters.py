from typing import List


class Solution:
    def isStrPresent(self, output_str, current_str):
        arr = output_str.split("_")
        # print(output_str)
        for char in current_str:
            for element_index in range(len(arr)):
                element = arr[element_index]
                if char in element:
                    return element_index
        return -1

    def maxLength(self, arr: List[str]) -> int:
        output_str = ""
        for index in range(0, len(arr)):
            isStr = self.isStrPresent(output_str, arr[index])
            isReplaced = False
            if isStr != -1:
                repeated_str = output_str.split('_')[isStr]
                if len(arr[index]) > len(repeated_str):
                    temp = output_str.split('_')
                    temp[isStr] = arr[index]
                    output_str = '_'.join(temp)
                    # print("1 - ", output_str)
                isReplaced = True
            if not isReplaced:
                output_str = output_str + arr[index] + "_"
            # print("2 - ",  output_str)

        return len(output_str.replace('_', ""))


if __name__ == "__main__":
    soln = Solution()
    output = ["cha","r","act","ers"]
    print("cha_r_act_ers".split("_"))
    print(soln.maxLength(output))