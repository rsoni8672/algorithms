class Solution:

    def get_closest_perfect_square(self, number, squares):
        if number == 1:
            return 0
        for index in range(len(squares)):
            if number == squares[index]:
                return index
            if number < squares[index]:
                return index - 1

    def get_least_numbers(self, n, squares, cache):
        print("Input number is - ", n)
        if n in cache:
            return cache[n]
        if n == 1:
            cache[1] = 1
            return 1
        if n == 0:
            cache[0] = 0
            return 0
        closest_square_index = self.get_closest_perfect_square(n, squares)
        mininum_num = 10000
        for index in range(closest_square_index, -1, -1):
            temp = self.get_least_numbers(n - squares[index], squares, cache)
            if temp < mininum_num:
                mininum_num = temp
        cache[n] = 1 + mininum_num
        return cache[n]
    def numSquares(self, n: int) -> int:
        cache = {}
        perfect_squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441,
                           484,
                           529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521,
                           1600,
                           1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025,
                           3136,
                           3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041,
                           5184,
                           5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569,
                           7744,
                           7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801, 10000]
        return self.get_least_numbers(n, perfect_squares, cache)

if __name__ == "__main__":
    solution = Solution()

    print(solution.numSquares(10000))
