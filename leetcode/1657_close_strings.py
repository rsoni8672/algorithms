class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq_map1 = {}
        freq_map2 = {}
        for letter in word1:
            freq_map1[letter] = freq_map1.get(letter, 0) + 1

        for letter in word2:
            if letter in word2:
                freq_map2[letter] = freq_map2.get(letter, 0) + 1

        arr1 = sorted(freq_map1.values())
        arr2 = sorted(freq_map2.values())

        for letter in freq_map1:
            if letter not in freq_map2:
                return False
        for letter in freq_map2:
            if letter not in freq_map1:
                return False

        return arr1 == arr2


if __name__ == "__main__":
    solution = Solution()
    word1 = "abc"
    word2 = "bca"
    print(solution.closeStrings(word1, word2))
