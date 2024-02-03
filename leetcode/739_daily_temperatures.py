from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answers = [0]*len(temperatures)
        for index in range(len(temperatures)):
            while len(stack) > 0 and temperatures[index] > temperatures[stack[-1]]:
                answers[stack[-1]] = index - stack[-1]
                stack = stack[:-1]
            stack.append(index)

        return answers

        answers = [0] * len(temperatures)
        next_index = {}

        temperature_map = {}
        for index in range(len(temperatures)):
            temperature = temperatures[index]
            temp = temperature_map.get(temperature, [])
            temp.append(index)
            temperature_map[temperature] = temp

        for temperature in temperature_map:
            next_index[temperature] = temperature_map[temperature][0]

        for index1 in range(len(temperatures)):
            current_temp = temperatures[index1]
            tempFound = False

            minimum_difference = len(temperatures)

            for next_temp in range(current_temp+1, 101):
                if next_temp in next_index:
                    if next_index[next_temp] - index1 < minimum_difference:
                        tempFound = True
                        minimum_difference = next_index[next_temp] - index1

            indexes = temperature_map[current_temp]
            indexes = indexes[1:]
            temperature_map[current_temp] = indexes
            if len(indexes) > 0:
                next_index[current_temp] = indexes[0]
            else:
                next_index.pop(current_temp)
            if tempFound:
                answers[index1] = minimum_difference
            else:
                answers[index1] = 0
        return answers
