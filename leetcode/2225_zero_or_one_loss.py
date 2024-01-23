from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost_players = {}
        players = set()
        for match in matches:
            players.add(match[1])
            players.add(match[0])
            lost_players[match[1]] = lost_players.get(match[1], 0) + 1

        output = [[], []]

        for player in players:
            if lost_players.get(player, 0) == 0:
                output[0].append(player)
            elif lost_players.get(player, 1) == 1:
                output[1].append(player)

        output[0] = sorted(output[0])
        output[1] = sorted(output[1])

        return output
