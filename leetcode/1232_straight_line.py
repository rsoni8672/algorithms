class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        init_x_difference = coordinates[1][0] - coordinates[0][0]
        init_y_difference = coordinates[1][1] - coordinates[0][1]

        if init_y_difference == 0:
            for coordinate in coordinates:
                if coordinate[1] != coordinates[0][1]:
                    return False
            return True

        slope = init_x_difference / init_y_difference

        for index in range(1, len(coordinates)):
            point1 = coordinates[index]
            point2 = coordinates[index - 1]

            x_difference = point2[0] - point1[0]
            y_difference = point2[1] - point1[1]
            if y_difference != 0:
                if x_difference / y_difference != slope:
                    return False
            else:
                return False
        return True