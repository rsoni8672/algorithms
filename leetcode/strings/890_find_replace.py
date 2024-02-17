from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        output = []
        for word in words:
            mapping = {}
            inverse_mapping = {}
            word_map = True
            inverse_map = True
            for index in range(len(word)):
                if pattern[index] in mapping:
                    if word[index] != mapping[pattern[index]]:
                        word_map = False
                        continue
                else:
                    mapping[pattern[index]] = word[index]

                if word[index] in inverse_mapping:
                    if pattern[index] != inverse_mapping[word[index]]:
                        inverse_map = False
                        continue
                else:
                    inverse_mapping[word[index]] = pattern[index]

            if word_map and inverse_map:
                output.append(word)
        return output


if __name__ == "__main__":
    words = ["a","b","c"]
    pattern = "a"
    solution = Solution()
    print(solution.findAndReplacePattern(words, pattern))
