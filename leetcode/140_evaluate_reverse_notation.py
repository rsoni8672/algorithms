from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['*', '+', '-', '/']
        if (len(tokens)) < 3:
            return int(tokens[0])

        for element in tokens:
            if element in operations:
                operand1 = stack[-1]
                operand2 = stack[-2]
                stack = stack[:-2]
                if element == '+':
                    stack.append(operand1+operand2)
                if element == '-':
                    stack.append(operand2 - operand1)
                if element == '*':
                    stack.append(operand1*operand2)
                if element == '/':
                    stack.append(int(operand2/operand1))
            else:
                stack.append(int(element))
        return int(stack[0])
if __name__=="__main__":
    soln = Solution()
    input = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(soln.evalRPN(input))
