from typing import List
import bisect


def alert_names(key_name: List[str], key_time: List[str]):
    def append_time(times_arr, time):
        bisect.insort(times_arr, time)
        return times_arr

    def time_diff_in_mins(time1, time2):
        mins1 = int(time1.split(":")[1])
        mins2 = int(time2.split(":")[1])
        hour1 = int(time1.split(":")[0])
        hour2 = int(time2.split(":")[0])

        if mins1 < mins2:
            mins_diff = 60 - mins2
        else:
            mins_diff = mins2 - mins1

        return (hour2-hour1)*60 + mins_diff

    times_map = {}

    def add_time(input_time):
        mins = (int(input_time.split(":")[1]) + 60) % 60
        hours = (int(input_time.split(":")[0])) + (int(input_time.split(":")[1]) + 60)//60

        if mins == 0:
            mins = "00"
        return str(hours) + ":" + str(mins)

    for index in range(len(key_name)):
        times = times_map.get(key_name[index], [])
        times = append_time(times, key_time[index])
        times_map[key_name[index]] = times

    output = []
    for person in times_map:
        times = times_map.get(person)
        for index in range(len(times)-2):
            time_diff = time_diff_in_mins(times[index], times[index + 2])
            if time_diff <= 60:
                output.append(person)
                break
    return sorted(output)


if __name__ == '__main__':
    print("output - ", alert_names(["daniel","daniel","daniel","luis","luis","luis","luis"]
,
                                   ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]))

# Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# Output: ["daniel"]
# Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
#
# Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
# Output: ["bob"]
# Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").