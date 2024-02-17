class Solution:

    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

    def countSubstrings(self, s: str) -> int:
        count = 0
        for index1 in range(len(s)):
            for index2 in range(index1 + 1, len(s) + 1):
                temp = s[index1:index2]
                print(temp)
                if self.is_palindrome(temp):
                    count = count + 1
        return count

    def get_palindromic_count(self, s, left, right):
        count = 0
        max_len = ""
        while left >= 0 and right <= len(s):
            if self.is_palindrome(s[left:right]) and left != right:
                if len(max_len) < len(s[left:right]):
                    max_len = s[left:right]
            left -= 1
            right += 1
        return max_len

    def count_substrings(self, s: str) -> int:
        ans = ""
        for index in range(len(s)):
            even_max = self.get_palindromic_count(s, index, index)
            odd_max = self.get_palindromic_count(s, index, index + 1)
            if len(even_max) < len(odd_max) and len(ans) < len(odd_max):
                ans = odd_max
            elif len(even_max) >= len(odd_max) and len(ans) > len(odd_max):
                ans = even_max
        return ans


if __name__ == "__main__":
    solution = Solution()
    s = ""
    print(solution.count_substrings(s))
