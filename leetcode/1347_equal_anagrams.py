class Solution:
    def get_freq(self, s):
        output = {}
        for char in s:
            output[char] = output.get(char, 0) + 1
        return output
    def minSteps(self, s: str, t: str) -> int:
        freq_s = self.get_freq(s)
        freq_t = self.get_freq(t)

        more_count = 0
        less_count = 0

        print(freq_s, freq_t)
        for freq in freq_t:
            if freq_t[freq] != freq_s.get(freq, 0):
                if freq_t[freq] > freq_s.get(freq,0):
                    more_count += freq_t[freq] - freq_s.get(freq, 0)
                elif freq_t[freq] < freq_s.get(freq, 0):
                    less_count += freq_s.get(freq, 0) - freq_t[freq]
        print("More count - ", more_count, " - Less count - ", less_count)
        for freq in freq_s:
            if freq_s[freq] != freq_t.get(freq, 0):
                if freq not in freq_t:
                    less_count += freq_s.get(freq, 0)
        print("More count - ", more_count, " - Less count - ", less_count)
        return min(more_count, less_count) + abs(more_count-less_count)


if __name__=="__main__":
    soln = Solution()
    s = "anagram"
    t = "mangaar"
    print(soln.minSteps(s, t))