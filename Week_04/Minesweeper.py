class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        m = len(board)
        n = len(board[0])
        def cal(i, j):
            count = 0
            for x in (-1, 1, 0):
                for y in (-1, 1, 0):
                    if x != 0 or y != 0:
                        if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] == 'M':
                            count += 1
            return count

        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'E':
                num_m = cal(i, j)
                if num_m > 0:
                    board[i][j] = str(num_m)
                    return
                else:
                    board[i][j] = 'B'
                    for x in (-1, 1, 0):
                        for y in (-1, 1, 0):
                            if x != 0 or y != 0:
                                dfs(x + i, y + j)
        dfs(x, y)
        return board
