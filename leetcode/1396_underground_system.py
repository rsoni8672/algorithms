class UndergroundSystem:

    def __init__(self):
        self.check_in_map = {}
        self.average_times = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        self.check_in_map[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        key = self.check_in_map[id][0] + "-" + stationName
        times = self.average_times.get(key, [])
        times.append([self.check_in_map[id][1], t])

        self.average_times[key] = times

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + "-" + endStation

        times = self.average_times[key]

        output = 0
        for time in times:
            output += (time[1] - time[0])

        return output/len(times)