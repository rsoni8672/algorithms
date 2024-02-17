class Solution:
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]

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

    def longestPalindrome(self, s: str) -> int:
        ans = ""
        for index in range(len(s)):
            even_max = self.get_palindromic_count(s, index, index)
            odd_max = self.get_palindromic_count(s, index, index + 1)
            # print(even_max)
            # print(odd_max)
            if len(even_max) < len(odd_max):
                if len(ans) < len(odd_max):
                    ans = odd_max
            else:
                if len(ans) < len(even_max):
                    ans = even_max
        return ans

if __name__ == "__main__":
    solution = Solution()
    s = "cbbd"
    print(solution.longestPalindrome(s))