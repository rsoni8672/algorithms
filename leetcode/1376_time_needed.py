from typing import List


class Solution:
    def numOfMinutes(self, n: int, head_id: int, managers: List[int], inform_time: List[int]) -> int:

        reportee_map = {}
        for employee_id in range(len(managers)):
            if managers[employee_id] != -1:
                temp = reportee_map.get(managers[employee_id], [])
                temp.append(employee_id)
                reportee_map[managers[employee_id]] = temp

        print(reportee_map)

        queue = []
        queue.append(head_id)

        times_array = [0] * len(managers)
        times_array[head_id] = 0

        while len(queue) > 0:
            manager = queue[0]
            queue = queue[1:]

            reporters = reportee_map.get(manager, [])

            for reporter in reporters:
                queue.append(reporter)
                times_array[reporter] = times_array[manager] + inform_time[manager]

        return max(times_array)


if __name__ == '__main__':
    solution = Solution()
    print(solution.numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0]))
