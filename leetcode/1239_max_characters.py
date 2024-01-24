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

    def isStrOverlap(self, characters, current_str):
        for character in current_str:
            if character in characters:
                return True

        return len(current_str) != len(set(current_str))
    def backtrack(self, characters, arr, index):
        if index == len(arr):
            return len(characters)
        result = 0
        if not self.isStrOverlap(characters, arr[index]):
            for character in arr[index]:
                characters.add(character)
            result = self.backtrack(characters, arr, index+1)
            for character in arr[index]:
                characters.remove(character)
        return max(result, self.backtrack(characters, arr, index+1))


        result = 0
    def maxLength(self, arr: List[str]) -> int:
        characters = set()

        backtrack(characters, arr, 0)



if __name__ == "__main__":
    soln = Solution()
    output = ["cha","r","act","ers"]
    print("cha_r_act_ers".split("_"))
    print(soln.maxLength(output))