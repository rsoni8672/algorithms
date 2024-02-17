from math import sqrt


class Solution:
    def isPrime(self, number):
        if number < 2:
            return False
        if number == 2:
            return True
        for index in range(number - 1, 1, -1):
            if number % index == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        nonPrimeNumbers = set()
        if n < 2:
            return 0
        for number in range(2, n-1):
            multiplier = 2
            temp = number
            while temp*multiplier < n:
                nonPrimeNumbers.add(temp*multiplier)
                multiplier += 1
            print(nonPrimeNumbers)
        return n - len(nonPrimeNumbers) - 2
if __name__ == "__main__":
    solution = Solution()
    print(solution.countPrimes(10))
