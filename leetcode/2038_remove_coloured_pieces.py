class Solution:
    def winner_of_game(self, colors: str) -> bool:
        player = 0

        a_index = 1
        b_index = 1

        last_played = None
        while a_index < len(colors) - 1 or b_index < len(colors) - 1:
            played = False
            if player == 0:
                player = 1
                while not played and a_index < len(colors) - 1:
                    if colors[a_index] == 'A' and colors[a_index - 1] == 'A' and colors[a_index + 1] == 'A':
                        played = True
                        a_index += 1
                        last_played = 0
                        break
                    a_index += 1
            else:
                player = 0
                while not played and b_index < len(colors) - 1:
                    if colors[b_index] == 'B' and colors[b_index - 1] == 'B' and colors[b_index + 1] == 'B':
                        played = True
                        b_index += 1
                        last_played = 1
                        break
                    b_index += 1

            if not played:
                if player == 0:
                    return True
                else:
                    return False
        if last_played is None:
            return False
        else:
            if last_played== 0:
                return True
            else:
                return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.winner_of_game("ABBBBBBBAAA"))
    print(solution.winner_of_game("AAABABB"))
    print(solution.winner_of_game("AA"))
