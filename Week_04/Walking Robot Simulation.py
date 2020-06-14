class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = ((0, 1), (1, 0),  (0, -1), (-1, 0))
        dx, dy = 0, 0
        di = 0
        distance = 0
        obstacles = set(tuple(obs) for obs in obstacles)
        for com in commands:
            if com == -2:
                di = (di + 3) % 4
            elif com == -1:
                di = (di + 1) % 4
            else:
                for _ in range(com):
                    new_x = dx + directions[di][0]
                    new_y = dy + directions[di][1]
                    if (new_x, new_y) in obstacles:
                        break
                    dx, dy = new_x, new_y
                    distance = max(distance, dx * dx + dy * dy)
        return distance

            