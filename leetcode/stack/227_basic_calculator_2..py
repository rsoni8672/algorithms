class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", '')
        print(s)
        arr = []
        last_digit = 0
        index = 0
        while index < len(s):

            char = s[index]
            if char in ('*', '/', '+', '-'):
                arr.append(char)
                index += 1
            elif char == ' ':
                print("here")
                index += 1
            else:
                last_digit = 0
                while index < len(s) and s[index] not in ('*', '/', '+', '-'):
                    last_digit = last_digit*10 + int(s[index])
                    index += 1
                arr.append(last_digit)
        print(arr)

        stack = []
        index = 0
        while index < len(arr):
            element = arr[index]
            if element in ('/', '*'):
                operand1 = int(stack[-1])
                stack = stack[:-1]
                operand2 = int(arr[index+1])
                index += 1
                if element == '/':
                    output = operand1/operand2
                    stack.append(int(output))
                if element == '*':
                    output = operand1*operand2
                    stack.append(int(output))
            else:
                stack.append(element)
            index += 1
        print(stack)
        answer = 0
        if len(stack) < 3:
            return stack[-1]
        for index in range(1, len(stack), 2):
            element = stack[index]
            if element == '+':
                answer += stack[index-1] + stack[index+1]
            if element == '-':
                answer += stack[index-1] + stack[index+1]
        return answer

if __name__=="__main__":
    solution = Solution()
    print(solution.calculate(" 3/2 "))


