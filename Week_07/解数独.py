class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for _ in range(9)]
        col = [set(range(1, 10)) for _ in range(9)]
        block = [set(range(1, 10)) for _ in range(9)]
        empty = []
        m = len(board)
        for i in range(m):
            for j in range(m):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    val = int(board[i][j])
                    b = i // 3 * 3 +j // 3
                    row[i].remove(val)
                    col[j].remove(val)
                    block[b].remove(val)

        def dfs(index = 0):
            if index == len(empty):
                return True
            i, j = empty[index]
            b = i // 3 * 3 +j // 3
            for val in row[i] & col[j] & block[b]:
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)
                if dfs(index + 1):
                    return True
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
                board[i][j] = '.'
            return False
        dfs()