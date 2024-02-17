class Solution:
    def reverseWords(self, s: str) -> str:
        index = 0
        while True:
            if s[index] == " " and s[index + 1] == " ":
                s = s[:index] + "" + s[index + 1:]
            else:
                index += 1
            if index == len(s) - 1:
                break
        s = s.strip()
        print(s)

        left = 0
        right = len(s) - 1
        while left < right:
            left_end = left
            while left_end < len(s) and s[left_end] != " ":
                left_end += 1
            print("1 - Left - ", s[left:left_end])
            left_word = s[left:left_end]

            right_start = right
            while right_start >= 0 and s[right_start] != " ":
                right_start -= 1
            print("2 -  Right - ", s[right_start + 1:right + 1])

            right_word = s[right_start + 1:right + 1]
            if left_end >= right_start + 1:
                s = s[:left] + right_word + s[right + 1:]
            else:
                s = s[:left] + right_word + s[left_end:right_start + 1] + left_word + s[right + 1:]
            print("3 - ", s)

            left = left_end + 1
            right_start += 1
            if len(right_word) > len(left_word):
                left_end += len(right_word) - len(left_word)
                right_start += len(right_word) - len(left_word)
                left = left_end + 1
                right = right_start - 2
            elif len(right_word) < len(left_word):

                left_end -= len(left_word) - len(right_word)
                right_start -= len(left_word) - len(right_word)
                left = left_end + 1
                right = right_start - 2
            else:
                left = left_end + 1
                right = right_start - 2
            print("4 - Left - ", left, "; Right - ", right)
        return s

if __name__ == "__main__":
    solution = Solution()
    string = "Alice does not even like bob"
    # string = "   fffff ff gg ee"
    # string = "a good   example"
    string = "the sky is blue"
    string = "hello world"
    print(solution.reverseWords(string))
