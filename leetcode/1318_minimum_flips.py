class Solution:
    def decimal_to_binary(num, output:str):
        if num >= 1:
            return Solution.decimal_to_binary(num // 2)
        output = output+str(num%2)
        return output

    def get_or_result(a, b):
        if a == '0' and b == '0':
            return '0'
        return '1'
    def minFlips(self, a: int, b: int, c: int) -> int:
        output = 0
        a = str(bin(a).replace("0b", ""))
        b = str(bin(b).replace("0b", ""))
        c = str(bin(c).replace("0b", ""))

        if len(a) > len(b):
            for index in range(len(a) - len(b)):
                b = "0" + b

        if len(a) < len(b):
            for index in range(len(b) - len(a)):
                a = "0" + a

        if len(a) > len(c):
            for index in range(len(a) - len(c)):
                c = "0"+c
        if len(c) > len(a):
            for index in range(len(c)- len(a)):
                a = "0"+a
                b = "0"+b

        print(a, b, c, sep='\n')
        min_val = min(len(a), len(c))
        for index in range(1, min_val+1):
            if c[-1*index] == '0':
                if a[-1*index] == '1':
                    output += 1
                if b[-1*index] == '1':
                    output += 1
            else:
                or_result = Solution.get_or_result(a[-1*index] , b[-1*index])
                if or_result != c[-1*index]:
                    output += 1

        return output


if __name__=='__main__':
    soln = Solution()
    print(soln.minFlips(8,3,5))

