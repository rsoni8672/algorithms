class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numbers_set = set(nums)
        answer = 0
        # print(len(numbers_set))
        while len(numbers_set) > 0:
            k = 1
            temp = 1
            number = numbers_set.pop()
            while number + temp in numbers_set.copy():
                numbers_set.remove(number+temp)
                k+=1
                temp+=1
            temp = 1
            while number-temp in numbers_set.copy():
                numbers_set.remove(number-temp)
                k+=1
                temp+=1
            answer = max(k,answer)
            if answer == len(nums):
                break
        return answer
if __name__=="__main__":
    solution = Solution()
    numbers=[1,2,3,4,5,6,77,8,9,10]
    print(solution.longestConsecutive(numbers))
